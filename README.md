## Proje Amacı

Bu projenin temel amacı, brute-force (kaba kuvvet) saldırılarının sistemler üzerinde
bıraktığı izleri incelemek ve bu tür saldırıların kimlik doğrulama
(authentication) logları üzerinden nasıl tespit edilebileceğini göstermektir.

Proje kapsamında, Linux tabanlı sistemlerde yaygın olarak kullanılan SSH / auth logları
analiz edilerek, kısa zaman aralıkları içerisinde aynı kaynaktan (IP adresinden)
gerçekleştirilen çok sayıda başarısız giriş denemeleri belirlenmeye çalışılmaktadır.

Odak noktası; savunma (defensive security) perspektifiyle,
saldırı davranışlarının sistem loglarında nasıl göründüğünü anlamak ve
bu davranışları anlamlı şekilde yorumlayabilmektir.

Proje, siber güvenlik alanında özellikle log analizi,
saldırı tespiti ve olay farkındalığı (incident awareness)
konularına giriş niteliğinde bir çalışma olarak tasarlanmıştır.

---

## Projenin Kapsamı

- SSH tabanlı kimlik doğrulama logları üzerinde çalışır  
- IP bazlı başarısız giriş denemelerini analiz eder  
- Zaman penceresi (time window) ve eşik değer (threshold) mantığı kullanır  
- Gerçek sistemlere müdahale etmez, yalnızca mevcut log dosyalarını inceler  

Bu yaklaşım, saldırıların **nasıl gerçekleştirildiğinden çok**
**nasıl fark edilebileceğine** odaklanır.

---

## Etik Kullanım Bildirimi

Bu araç yalnızca eğitim ve savunma amaçlı olarak geliştirilmiştir.
Gerçek sistemlere saldırmak, yetkisiz erişim denemeleri yapmak veya
zarar verici faaliyetlerde bulunmak için tasarlanmamıştır.

Projenin amacı; siber güvenlik alanında etik sınırlar içerisinde
bilgi edinmek, savunma mekanizmalarını anlamak ve
güvenli sistem tasarımı konusunda farkındalık oluşturmaktır.

---

## Gereksinimler (Requirements)

- Python 3.8 veya üzeri  
- Standart Python kütüphaneleri  
- Linux tabanlı SSH / auth log formatı  
  (örnek log dosyaları proje içerisinde sağlanmaktadır)

Herhangi bir üçüncü parti kütüphane zorunlu değildir.
Proje, temel Python yetenekleri ile anlaşılabilir ve geliştirilebilir
olacak şekilde tasarlanmıştır.

---

## Sınırlamalar

- Dağıtık (distributed) brute-force saldırıları bu yaklaşım ile
  her zaman tespit edilemeyebilir  
- Düşük hızda (low-and-slow) gerçekleştirilen denemeler,
  yanlış negatif sonuçlara yol açabilir  
- Bu proje, gerçek bir SIEM veya IDS sisteminin yerine geçmez  

Bu sınırlamalar bilinçli olarak belirtilmiştir ve projenin
bir öğrenme ve farkındalık çalışması olduğu göz önünde bulundurulmalıdır.
