# Garmin Run: peta kemampuan dan ruang kombinasi

19 Oktober 2026. Fokus: structured workout sportTypeId 1/running. Baca bersama `AI-COACH-BRIEF.md`.

## Bukti yang sudah ada

- Live: GET `/workout-service/workout/types` dan `/workout-service/workout/types/sport` sama-sama HTTP 200. Snapshot `workout-types.json`, `workout-sports.json`, `metadata-status.json`.
- Kamus global saat diperiksa: 8 step types, 24 condition types, 27 target types, 12 sport types. Daftar global mencakup swim, strength, cycling dan fitur lain; bukan matriks izin running.
- Live create + GET readback: workout <WORKOUT_ID>, satu langkah run, waktu 1200 detik, tanpa target. Hanya fixture itu yang sudah terbukti tersimpan; tidak ada pengujian kombinasi baru pada tahap riset ini.
- APK: serializer, enum, editor running, repeat dan target sekunder dianalisis. Peringatan/dekompilasi tidak lengkap tetap dipertahankan dalam sumber.
- Belum ada uji FIT atau penerimaan/eksekusi di jam.

## Model komposisi

```text
Workout running
  └─ segment(s)
       └─ langkah linear atau grup repeat
            ├─ peran: warmup/run/walk/recovery/rest/cooldown/other
            ├─ selesai kapan: waktu/jarak/Lap/kalori/ambang HR
            ├─ target utama: none/pace/cadence/HR/power
            ├─ opsional target sekunder yang kompatibel
            └─ catatan; opsi repeat/perangkat tertentu
```

Nilai numerik, banyak langkah, susunan blok, jumlah pengulangan dan target berbeda membuat jumlah kemungkinan praktis tidak bisa dinyatakan sebagai satu daftar kombinasi valid. `combination-matrix.csv` berisi **245 sel riset** (7 peran × 5 kondisi × 7 mode target), bukan 245 workout yang sudah diterima server. Nilai, pasangan target sekunder dan repeat adalah dimensi tambahan.

## Peran langkah

| Peran | JSON stepTypeId | Catatan |
|---|---:|---|
| Warmup | 1 | Boleh waktu, jarak, atau Lap sesuai opsi editor |
| Cooldown | 2 | Target dan kondisi selesai terpisah dari perannya |
| Run/interval | 3 | Label run pada editor running; bukan berarti harus sesi intensif |
| Recovery | 4 | Blok pemulihan di antara repetisi |
| Rest | 5 | Berbeda dari rest day; ini langkah dalam workout |
| Repeat | 6 | Container, bukan langkah lari biasa |
| Other | 7 | Instruksi langkah khusus |
| Main | 8 | Ada di kamus global; tidak muncul pada daftar peran running yang dianalisis |
| Walk | alias 4, aliasId 100 di enum Android | Bukan ID backend baru 100. Representasi lengkap category/exercise/instruction perlu fixture live, jangan samakan dengan recovery biasa secara diam-diam |

Peran bukan batas intensitas fisiologis. Nama `interval` pada JSON tidak membuktikan latihan tersebut tempo/VO2max.

## Kondisi selesai

| Kondisi | conditionTypeId | Bentuk dan batas bukti |
|---|---:|---|
| Lap button | 1 | Terbuka sampai pengguna menekan Lap; jangan beri perkiraan waktu pasti |
| Time | 2 | `endConditionValue` detik; 1200 sudah live-tested |
| Distance | 3 | Meter; nilai/UI/hasil FIT perlu fixture |
| Calories | 4 | Ada pada editor umum endurance; bukan pilihan default untuk dosis latihan coach |
| HR threshold | 6 | Ambang HR, opsional `endConditionCompare`; nama operator dan makna tepatnya perlu fixture |
| Power threshold | 5 | Ada pada cabang cycling di editor; jangan otomatis membuka untuk running |
| Iterations | 7 | Untuk repeat, bukan durasi sebuah langkah run |
| Fixed rest/repetition/reps dll | 8+ | Kamus lintas olahraga; tidak diaktifkan untuk running tanpa bukti |

Bukti opsi kondisi: `sources/...workouts.presentation.stepedit.h.java`, metode `e` sekitar baris 1606–1616. Sebagian metode gagal didekompilasi penuh; cabang daftar terlihat, tetapi ini bukan bukti semua pasangan input diterima server.

## Target utama running

| Mode | workoutTargetTypeId | Field inti | Status |
|---|---:|---|---|
| None | 1 | tanpa range/zone | Fixture waktu 20 menit sudah live |
| Pace range | 6 | targetValueOne/Two | Editor Android + pembanding client; belum fixture live |
| Cadence | 3 | targetValueOne/Two | Kandidat steps/min; konvensi perangkat perlu verifikasi |
| HR zone | 4 | zoneNumber | Zona running milik atlet; UI 1–5 |
| Custom HR | 4 | targetValueOne/Two | Kandidat bpm; validasi range dan metode zona terpisah |
| Running power zone | 2 | zoneNumber | UI 1–5, feature-gated |
| Custom running power | 2 | targetValueOne/Two | Kandidat watts, feature-gated; jangan memakai batas UI sebagai rekomendasi aman |

Running walk mempunyai cabang target khusus; pilihan power tidak tercantum pada cabang itu. Ada target instruction 19 untuk walk effort, tetapi encoding cue dan kompatibilitas jam belum diuji. Running power muncul melalui feature flag `bo1...t0()`; daftar UI tidak otomatis membuktikan sensor/model jam pengguna mendukungnya.

Persentase HR/power mempunyai jejak field unit `percent` di serializer, tetapi belum ada pemetaan lengkap basis referensi (max HR/LTHR/FTP), pasangan field dan hasil live. Statusnya riset, tidak boleh diganti menjadi angka absolut tanpa basis pengguna yang jelas. RPE/talk-test adalah cue coach; belum ada bukti target numerik RPE running native yang universal. Simpan cue sebagai catatan dan gunakan target none bila tepat.

Speed, grade, lap-average targets, power curve dan resistance muncul dalam kamus global. Belum dibuktikan sebagai pilihan primer running pada cabang editor ini. Hill workout berarti memilih bukit yang sesuai dan mengatur waktu/jarak/effort; bukan menjanjikan jam otomatis mengatur kemiringan.

## Target sekunder

Serializer mendukung `secondaryTargetType`, `secondaryTargetValueOne/Two`, `secondaryZoneNumber`, `secondaryTargetValueUnit`, serta field power curve sekunder. `o62.u0.b` memuat none/pace/cadence/HR zone/custom HR/run power zone/custom power sebagai daftar kandidat.

Jangan mengasumsikan seluruh pasangan primer × sekunder legal. `x52.f.a()` mengelompokkan target yang saling tumpang tindih dan cabang UI bergantung sport/duration. Contoh pace+HR adalah kandidat berguna, tetapi penerimaan server, tampilan FIT, dan dukungan jam harus dibuktikan. Pilih satu target dulu untuk MVP; jangan memecah dua target menjadi dua langkah karena itu mengubah dosis latihan.

## Repeat, blok dan variasi sesi

- Fixed count: `RepeatGroupDTO`, `numberOfIterations`, nested `workoutSteps`.
- Until time: serializer memiliki cabang repeat dengan `endCondition` time dan nilai waktu.
- Nested repeat: struktur tree dan serializer stack terlihat; kedalaman maksimal dan dukungan perangkat belum diketahui.
- `skipLastRestStep`: terlihat di serializer, semantik langkah terakhir harus dicek pada readback/FIT/jam.
- `smartRepeat`: field ada, arti produk dan kompatibilitas belum cukup untuk diaktifkan otomatis.
- Repeat-until distance/calories/HR/power tersedia pada spesifikasi FIT; **tidak** otomatis berarti endpoint JSON native Android menyediakan semua itu.

Contoh keluarga yang dapat diekspresikan: easy, recovery run, long run, steady/progression, tempo kontinu, cruise intervals, repetisi berbasis waktu/jarak, strides, fartlek, hill repeats, run–walk, ladder/pyramid, blok berbeda, serta sesi pace/HR/power. Kategori coaching tersebut bukan API enum. Masing-masing merupakan susunan blok di atas.

`coach-intent-examples.json` berisi 12 contoh struktur, bukan resep personal dan belum di-upload. `effort_text` adalah konsep internal coach yang harus dikompilasi menjadi description + target none, bukan field target Garmin.

## Satuan dan struktur yang harus dijaga

- Time: detik. Distance: meter. Tampilan km/mile/minute bukan nilai wire.
- Pace: m/s, bukan angka seperti 6.5 atau string 6:30. Contoh 6:00–6:30/km menjadi lower speed 2.56410256 dan upper speed 2.77777778 m/s. Batas kecepatan terbalik terhadap urutan cepat/lambat pace. Lihat `pace-conversion-example.json`.
- HR/power zones merujuk konfigurasi atlet. Zone 2 tidak mempunyai bpm/watt universal.
- Jangan memberi offset FIT +100 bpm/+1000 watt langsung pada JSON Connect. Aturan penyimpanan FIT dan JSON berbeda.
- Workout JSON memakai segmentOrder mulai 0. Serializer mengatur stepOrder/childStepId dan grup repeat; urutan internal repeat perlu fixture asli. Jangan menganggap preorder traversal sederhana selalu sama dengan encoding Garmin.
- Batas publik custom workout: maksimum 50 langkah menurut support Garmin; cara menghitung grup, children dan ekspansi repeat perlu cek terhadap model jam. Gunakan batas konservatif dan verifikasi serialisasi, jangan mengklaim 50 repetisi = 50 slot.
- Open/Lap dan HR-threshold dapat membuat durasi total tidak pasti. Bedakan fixed duration, estimated duration, dan unknown.
- API menerima JSON ≠ FIT benar ≠ jam menerima ≠ latihan selesai.

## Sumber

- Snapshot metadata live dan APK di folder ini; `../sources/...model.j0.java:423`, `...model.h0.java:454`, `...stepedit.h.java:1595,2231`; `sources/x52.f.java`, `sources/o62.u0.java`.
- [Garmin custom workout support](https://support.garmin.com/en-CA/?faq=wZ52AaLbLG2GC1Lxu2l4k7&identifier=777730&tab=topics): jumlah langkah, range target, target sekunder bergantung perangkat.
- [Garmin FIT workout format](https://developer.garmin.com/fit/articles/file-types/workout.html): target zone/custom, repeat dan pemisahan intensitas/durasi. Ini spesifikasi FIT, bukan kontrak JSON Connect.
- Package lokal garminconnect 0.3.19 `workout.py`: pembanding pace_to_mps dan model target. Pembanding tidak menggantikan bukti API/jam.

## Urutan validasi berikutnya

1. Inventaris model jam/sensor dan zona running pengguna.
2. Satu scratch workout yang diperbarui secara terkontrol untuk fixture: distance-none; Lap warmup; pace; HR zone; custom HR; cadence; fixed repeat; skip-last; dua target; power hanya jika supported.
3. Untuk setiap fixture: POST/PUT → GET semantic comparison → unduh FIT dan decode → kirim/cek pada jam bila tahap itu diminta.
4. Pisahkan test negatif (range terbalik, zone hilang, tree terlalu dalam, field swim) dari percobaan ke server; tolak lokal lebih dahulu.
5. Baru promosikan fitur dari candidate → server_verified → fit_verified → device_verified dalam manifest. Jangan meng-upload seluruh kombinasi matriks untuk brute force.

## Historical server-only follow-up

Fixed repeat and distance/pace templates were created and semantically read back in separately authorized tests. Identifiers, personal targets and raw artifacts are withheld. FIT/device verification remains unperformed. The candidate matrix is not a compatibility guarantee.
