# Arahan AI coach runner

## Tujuan produk

Agent menjadi coach yang memahami tujuan dan keadaan atlet, memutuskan sesi yang masuk akal, lalu langsung membuat structured workout Garmin dalam ruang otonomi yang disetujui pengguna. Memilih **rest/no workout** harus menjadi hasil yang sah. Fitur awal berjalan on-demand; penjadwalan otomatis/monitoring harian belum diminta atau dibuat.

## Arsitektur yang disarankan

```text
Arahan pengguna + profil + riwayat latihan + feedback terbaru
  → AI coach: keputusan dan alasan + CoachIntent terstruktur
  → policy validator: dosis, konteks, otonomi dan kelengkapan data
  → deterministic compiler: CoachIntent → Garmin JSON
  → capability validator: server/FIT/jam dan dukungan fitur
  → Garmin adapter: create → GET readback
  → status hasil; schedule/send hanya sesuai otorisasi terpisah
  → setelah aktivitas: bandingkan planned vs actual + feedback
```

LLM memilih sesi dan menjelaskan alasan. Compiler menangani ID enum, unit, pace conversion, repeat indexing dan payload. Adapter memegang token, melakukan HTTP, serta rekonsiliasi timeout. LLM tidak menerima raw token/password dan tidak mengarang respons server.

## Kontrak data sebelum coach boleh menentukan sesi personal

Profil yang dikonfigurasi sekali: tujuan/event/tanggal, pengalaman, ketersediaan hari dan durasi, preferensi long run, model jam/sensor, akses treadmill/track/bukit, batas volume/intensitas yang disepakati, riwayat masalah yang relevan menurut pengguna, zona HR/power/pace beserta metode dan tanggal sumbernya.

Konteks tiap keputusan: riwayat beberapa minggu dengan jenis/intensitas/durasi/jarak; sesi terakhir dan apakah selesai; perubahan beban; tidur/pemulihan bila tersedia; feedback lelah/nyeri/sakit/kesiapan; cuaca/medan bila memengaruhi rencana. Tidak semua data wajib tersedia, tetapi missing/stale harus terlihat dan mengurangi keyakinan/otonomi. Pembacaan aktivitas dan health metrics yang belum dilakukan perlu scope akses jelas pada implementasi berikutnya.

Jangan mengarang threshold, HR max, LTHR, FTP, atau pace balapan. Jangan menyamakan training readiness Garmin dengan izin medis. Bila data penting untuk target personal belum ada, pilih draft tanpa angka target atau minta hanya data yang mengubah keputusan. Nilai contoh JSON dalam riset bukan rekomendasi pengguna.

## CoachIntent: output AI sebelum menjadi Garmin JSON

```json
{
  "action": "create_workout",
  "objective": "easy aerobic session",
  "rationale": "Explain using actual recent training and user constraints",
  "data_as_of": "ISO timestamp",
  "confidence": "medium",
  "assumptions": [],
  "sport": "running",
  "name": "AI Coach - session name",
  "steps": [
    {
      "kind": "step",
      "role": "run",
      "end": {"kind": "time", "seconds": 1200},
      "target": {"kind": "none"},
      "cue": "Effort cue chosen for the athlete"
    }
  ],
  "delivery": {"create": true, "schedule": false, "send_to_device": false}
}
```

Contoh menunjukkan bentuk kontrak, bukan pemilihan latihan personal. Alternatif action: `rest`, `draft`, `need_input`. `rest` tidak menjadi workout nol menit. Representasi repeat memakai `kind: repeat`, `count`, dan `steps` sesuai contoh struktur di folder ini.

## Otonomi yang cocok untuk kebutuhan pengguna

Setelah profil dan batas operasional disepakati, `auto_create` dapat diaktifkan. Coach boleh langsung membuat sesi dalam batas itu tanpa konfirmasi berulang. Ia tetap harus menyampaikan apa yang dibuat dan alasannya. Schedule dan send-to-watch merupakan izin terpisah; auto_create tidak otomatis mengaktifkan keduanya.

Policy disimpan sebagai konfigurasi terstruktur, bukan hanya paragraf prompt: `max_sessions_per_day`, batas durasi/jarak mingguan yang personal, jumlah sesi intensif, aturan jarak antar sesi berat, fitur Garmin yang sudah tervalidasi, masa berlaku data, dan scope delivery. Angka tersebut belum ditetapkan untuk pengguna ini. Jangan memakai angka UI Garmin sebagai batas dosis coach. Hindari aturan kenaikan beban universal yang dianggap aman untuk semua atlet.

Jika input tidak lengkap atau policy belum dikonfigurasi, agent boleh mempelajari/membuat draft, tetapi tidak menyebutnya sebagai resep personal yang telah disesuaikan. Nyeri/keluhan yang mengkhawatirkan atau sakit mengubah keputusan menjadi berhenti/need_input, bukan menyiasati batas agar tetap menghasilkan workout.

## Aturan compiler dan adapter

- Strict schema dan allowlist sport running; tolak field swim/strength yang tersisip.
- Semua angka finite; waktu/jarak positif; range tidak terbalik; zona punya sumber atlet yang sah.
- Konversi pace deterministik; uji 6:00–6:30/km dan satuan mile.
- Validasi tree, repeat count/depth, indeks unik, hitung batas langkah dan dosis termasuk repeat.
- Selaraskan target ganda; jangan diam-diam membuang target sekunder/fitur yang tidak didukung.
- Capability evidence terpisah untuk server, FIT dan jam. Sebagian besar kombinasi masih candidate.
- Setiap publikasi memiliki request_id, athlete_id internal, hash intent, status dan workoutId. Lock per request; pencarian/rekonsiliasi sebelum mencoba ulang POST yang hasilnya ambigu. Nama unik saja belum cukup sebagai idempotency.
- Simpan ringkasan audit dan payload yang sudah disaring. Jangan mencatat token, cookie, password, atau health data mentah tanpa kebutuhan.
- Sukses hanya setelah GET readback sesuai makna intent, termasuk repeat/range/unit. Jika create sudah berhasil tetapi readback gagal, status `created_unverified`, bukan membuat ulang.
- Pisahkan `created`, `scheduled`, `queued_to_device`, `device_received`, dan `completed_activity`.

## Prompt awal agent

> Kamu adalah AI running coach untuk atlet pemilik akun ini. Tugasmu memilih rest atau sesi lari berdasarkan tujuan, profil, riwayat dan feedback aktual. Patuhi CoachPolicy, DataFreshnessPolicy dan GarminCapabilityManifest yang diberikan sebagai konfigurasi. Jangan mengarang data atlet atau dukungan fitur perangkat. Jelaskan alasan singkat dan hasilkan CoachIntent terstruktur. Jika auto_create diizinkan dan semua validasi lulus, panggil tool create_running_workout sekali dengan request_id stabil. Baca hasil verifikasi; laporkan workoutId hanya dari tool. Bila data esensial hilang, keluarkan need_input atau draft dengan pertanyaan paling relevan. Jangan menentukan sendiri angka zona/threshold dari contoh, jangan memperlakukan rest sebagai kegagalan. Jangan schedule atau send kecuali scope delivery mengizinkannya. Setelah aktivitas nyata tersedia, evaluasi planned versus actual beserta feedback; sesuaikan keputusan berikutnya tanpa menyembunyikan ketidakpastian.

## MVP dan urutan kerja

1. **Capability research**: hasil tahap ini sudah tersedia; 245 sel kandidat dan 12 contoh intent.
2. **Workout engine**: strict schema + compiler + unit tests + create/readback idempotent. Prioritas time/distance/Lap, none/pace/HR, fixed repeat; power/secondary/nesting belakangan.
3. **Validasi Garmin**: fixture server, FIT, kemudian jam. Tentukan model jam sebelum mempromosikan device compatibility.
4. **Coach v1**: profil pengguna + data latihan yang diizinkan + keputusan on-demand; jalankan draft mode sampai kualitas keputusan dinilai pengguna, lalu auto_create dalam policy.
5. **Feedback loop**: aktivitas yang selesai, RPE/feedback dan penyesuaian sesi berikutnya. Monitoring berkala hanya bila diminta.

Data pengguna yang dibutuhkan untuk memulai personalisasi: target utama/event, pengalaman dan volume beberapa minggu terakhir, hari tersedia, model jam, zona yang dipakai, serta batas otonomi (create saja atau termasuk schedule/send). Belum diisi atau diasumsikan dalam riset ini.
