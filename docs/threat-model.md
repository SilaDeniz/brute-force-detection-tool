## Asset

Bu projede korunması hedeflenen temel varlık,
sistem üzerinde yer alan kullanıcı hesapları ve
bu hesaplara ait kimlik doğrulama süreçleridir.

## Threat Actor

Tehdit aktörü, otomatik araçlar kullanarak
SSH servisleri üzerinden çok sayıda parola denemesi
gerçekleştiren saldırgandır.

## Attack

Saldırı, kısa zaman aralıkları içerisinde
aynı IP adresinden tekrarlanan başarısız
kimlik doğrulama denemeleri şeklinde gerçekleşmektedir.
Bu davranış brute-force saldırılarına işaret eder.

## Detection Idea

Kimlik doğrulama logları analiz edilerek,
belirli bir zaman penceresi içerisinde
aynı kaynaktan gelen başarısız giriş denemelerinin
sayısı takip edilir.
Belirlenen eşik değerin aşılması durumunda
şüpheli davranış olarak işaretlenir.

## Limitations

Dağıtık kaynaklardan gerçekleştirilen saldırılar
veya düşük hızda yapılan denemeler bu yaklaşım
ile her zaman tespit edilemeyebilir.
Bu nedenle proje, tek başına tam bir güvenlik çözümü
olarak değil, destekleyici bir tespit mekanizması
olarak değerlendirilmelidir.

