# Alur autentikasi Garmin Connect Android 5.30.1

Analisis 19 Oktober 2026 atas APK asli dari ADB. App pada perangkat sudah login saat inspeksi; sesi yang ada tidak dihapus dan aplikasi tidak di-logout. Metadata live WebView: `com.google.android.webview` 155.0.8059.43. ADB dipakai untuk memperoleh APK dan membaca status perangkat, bukan mengambil password/token dari private storage.

## Cabang yang dikonfigurasi aplikasi

`fq1.n.b` (metadata `MobileAuthInitializer`) membuat `SSOPortalConfig` dan memasangnya pada `AuthenticationHelper`. Konfigurasi produksi:

- Theme: DARK (resource `ssoTheme`).
- Client: `GCM_ANDROID_DARK` (LIGHT juga dikonfigurasi).
- Service URL: `https://mobile.integration.garmin.com/gcm/android`.
- URL login: `https://sso.garmin.com/mobile/sso/{locale}/sign-in?clientId=GCM_ANDROID_DARK`.

Bukti: `auth-sources/fq1.n.java:288`, `auth-sources/af2.g.java:14`, `auth-sources/ve2.l.java` metode `e`, `f`, `g`. `ve2.l.g()` bernilai true bila konfigurasi portal ada. `AuthenticationActivity` memisahkan SIGN_IN_PORTAL dari SIGN_IN lama. File Java hasil JADX beberapa kali salah memilih alias/import untuk nama pendek yang bentrok; `AuthenticationActivity.smali` mempertahankan descriptor DEX asli, termasuk `Laf2/g;`, bukan coroutine `Lo53/g;` yang muncul di dekompilasi Java.

## Login portal dan JavaScript bridge

Android memakai WebView dengan JavaScript dan DOM storage aktif. Portal mengirim event melalui:

```javascript
window.GMNEventHandler.handleEvent(JSON.stringify(event))
```

Event autentikasi:

```json
{
  "eventType": "USER_AUTHENTICATED",
  "flowName": "AUTHENTICATION",
  "data": {
    "serviceTicket": "<ephemeral service ticket>",
    "serviceUrl": "https://mobile.integration.garmin.com/gcm/android"
  }
}
```

`PortalJsMessageHandler` (`af2.e`) menaruh event dalam antrean. `MobileAuthAbstractPortalWebFrag` (`af2.c`) mengonsumsi USER_AUTHENTICATED dan meneruskan service URL/ticket ke pemroses autentikasi. MFA dan consent berjalan pada halaman resmi Garmin. Tidak perlu menebak format POST login dari library iOS.

Pembacaan tanpa kredensial atas URL portal produksi mengembalikan HTTP 200. JavaScript resmi `/mobile/assets/index-d10b89ff39a6804af60e44186d1f4230.js` juga menunjukkan bridge GMNEventHandler, USER_AUTHENTICATED dan field serviceTicket/serviceUrl. Hash bundle dapat berubah; ini adalah snapshot sesi ini.

## Pertukaran ticket ke token API

Jejak: `te2.o1` → `te2.p1` (`ITTicketForCredentialExchanger.forDI2`) → `pc2.p` (`ITTicketForDI2Request`) → `pc2.a` / `pc2.b`.

```text
POST https://diauth.garmin.com/di-oauth2-service/oauth/token
Content-Type: application/x-www-form-urlencoded
Authorization: Basic base64(client_id + ':' + optional_client_secret)

client_id=<Android DI client ID>
service_ticket=<ticket from portal>
grant_type=https://connectapi.garmin.com/di-oauth2-service/oauth/grant/service_ticket
service_url=https://mobile.integration.garmin.com/gcm/android
```

`pu.b.a` menentukan konfigurasi DI; PROD memakai nilai StringRetriever index 7 ditambah `_2025Q2`, tanpa secret pada konstruktor OAuth2Client. Base ID `GARMIN_CONNECT_MOBILE_ANDROID_DI` belum didekode langsung dari StringRetriever APK; nama ini dikonfirmasi silang dari konstanta library Python 0.3.19. Jadi ID lengkap yang dipakai percobaan adalah kandidat yang didukung dua petunjuk, bukan hasil capture token request Android live.

## Validasi aplikasi asli

Initializer memasang `nc2.c` (`GoogleIntegrityTokenProvider`), cloud project number 749008027698. Provider menghitung SHA-256 request body dan meminta Standard Play Integrity token dengan requestHash. `pc2.a` mengirim:

- `app-validation`: token yang diperoleh provider; atau
- `app-validation-error`: informasi kegagalan provider, bila tersedia.

Keberadaan kode ini tidak membuktikan header tersebut selalu diwajibkan oleh server. Pengujian di luar aplikasi tidak memiliki provider Play Integrity Garmin yang sah. Skrip tidak mengarang header, mengekstrak/replay attestation, atau menonaktifkan validasi.

## Pengujian yang disiapkan

`tools/android_portal_create.py` membuka halaman resmi memakai Chrome lokal dan memasang receiver bridge GMNEventHandler agar event portal diterima seperti antarmuka WebView. Pengguna memasukkan kredensial langsung di halaman Garmin; skrip tidak membaca field login dan tidak menyimpan password/MFA/service ticket.

Sesudah USER_AUTHENTICATED:

1. Satu POST pertukaran service ticket ke endpoint DI di atas.
2. GET daftar workout dengan Bearer access token untuk membuktikan autentikasi API.
3. Satu POST create workout running 1200 detik.
4. GET workout berdasarkan ID dan validasi nama/sport/durasi/target.

Nama unik: `REA - Android API Test <run_id>`. Tidak menjadwalkan atau mengirim ke jam. Status aktual dan daftar status HTTP yang disaring: `.private/android-live-create/result.json`. Respons create/readback hanya disimpan jika tahap itu benar-benar dijalankan. Token API yang berhasil diterima, bila ada, disimpan terpisah di `.private/android-token.json` mode 600.

Perbedaan terhadap Android asli dicatat dalam result.json: Chrome desktop menggantikan WebView; User-Agent riset, bukan salinan header native; kandidat base DI client ID; tidak ada Play Integrity token native. Ini uji reproduksi alur portal/grant backend, belum bukti reproduksi seluruh karakteristik aplikasi Android.

Rujukan implementasi pembanding: https://github.com/cyberjunky/python-garminconnect . Tidak menggunakan strategi/fallback login library tersebut untuk percobaan Android ini.

## Historical test outcome (sanitized)

The official portal → DI token → authenticated workout read → create → GET semantic readback flow succeeded in an earlier authorized test. No workout identifier, name, session, ticket or response artifact is published. Schedule and watch delivery were not tested. This does not establish lasting acceptance or a universal attestation policy.
