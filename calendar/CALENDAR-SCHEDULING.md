# Menghubungkan workout ke kalender Garmin

Diperiksa 19 Oktober2026; read-only, tidak menambah jadwal baru.

## Kontrak Android

POST `https://connectapi.garmin.com/workout-service/schedule/{workoutId}`
Authorization bearer sesi lokal; Content-Type application/json.
Body adalah JSON STRING tanggal: `"2026-10-20"`, bukan `{ "date": "2026-10-20" }`.
Tanggal di atas hanya contoh, belum pilihan pengguna atau request yang dieksekusi. Date-only tanggal kalender pengguna, tidak dikonversi menjadi UTC midnight.

Bukti source:
- ../sources/l52.x.java86–87 POST ke schedule/{workoutId}, RequestBody dateTime.
- ../sources/com.garmin.android.apps.connectmobile.workouts.presentation.details.WorkoutDetailsActivity.java715: DateTime diformat dengan pola `\"yyyy-MM-dd\"` (literal quotes).
- ../sources/com.garmin.android.apps.connectmobile.workouts.presentation.details.s.java119–124 meneruskan string ke repository.j.
- ../sources/l52.z.java404–405 RequestBody dibuat langsung dari string.
- ../sources/l52.a0.java56 memanggil service.e(workoutId,body).
- ../sources/com.garmin.android.apps.connectmobile.workouts.data.model.WorkoutScheduleDTO.java85+ membaca workoutScheduleId,calendarDate,createdDate,nested workout.

## Historical read verification (sanitized)

Summary, month-grid and existing-schedule GETs returned HTTP 200 in an authorized read-only test. Calendar entries, counts, dates and identifiers are withheld. October uses month index 9 in the observed route. Schedule IDs and template workout IDs are distinct.

## Alur implementasi

1. Pilih workoutId dan tanggal konkret dari pengguna. Riset kontrak bukan izin untuk menulis jadwal.
2. Baca kalender bulan tujuan, filter itemType workout, workoutId dan date. Kalau sudah ada, gunakan schedule ID tersebut; jangan buat duplikat diam-diam.
3. Simpan operation lokal serta snapshot sebelum POST. POST sekali, body json.dumps(dateString). POST diterima/error ambigu jangan replay otomatis: baca ulang kalender untuk mencari entri baru yang cocok dibanding snapshot. Jika belum jelas, berhenti unresolved.
4. Ambil workoutScheduleId hasil POST lalu GET `/workout-service/schedule/{workoutScheduleId}`. Cocokkan calendarDate dan nested workout.workoutId.
5. Baca kalender lagi dan cocokkan itemType workout, workoutId,date,id. Ini bukti calendar-attached.
6. Schedule bukan bukti sudah tersinkron ke jam; device delivery adalah operasi terpisah.

DELETE `/workout-service/schedule/{scheduleWorkoutId}` ditemukan di Android; belum diuji. Menghapus jadwal memakai schedule ID, bukan template workout ID. Jangan menghapus workout atau jadwal lama untuk test.

PUT `/workout-service/schedule/sendtodevices` dan POST `/mobile-gateway/calendar/schedule-workout/device/{deviceId}` ada di Android, belum diuji dan bukan diperlukan sekadar attach calendar. Jangan campur dengan trainingplan-service/addWorkoutTask yang digunakan untuk training plan tertentu.

## Status bukti

Kontrak POST/date-string: ditemukan dan ditelusuri di Android. Tiga jalur GET kalender/summary/schedule: live200. Membuat schedule baru: belum diuji karena tanggal belum ditentukan. Penerimaan jadwal di jam: belum diuji.

Raw local artifacts and the account-specific helper are intentionally not published. Source references above require separately obtained local extraction inputs.
