🖼️ WEBP TO PNG CONVERTER

Bu Python script'i, bir klasördeki **tüm `.webp` dosyalarını** otomatik olarak **`.png` formatına** dönüştürür.  
Alt klasörlerdeki dosyalar da taranır ve aynı isimde dosya varsa `(1), (2)` şeklinde numaralandırılır.

------------------------------------------------------------
✨ NEDEN BU ARACI KULLANMALISINIZ?
------------------------------------------------------------
🔹 **WebP formatı** web sitelerinde yaygın olarak kullanılır çünkü dosya boyutları küçüktür ve daha hızlı yüklenir.  
🔹 Ancak bazı grafik programları veya uygulamalar WebP formatını desteklemez.  
🔹 İşte tam burada bu script devreye girer!  

💡 Bu araç sayesinde:
- WebP dosyalarını kolayca PNG formatına dönüştürebilirsiniz.
- Tek tek dönüştürme zahmetinden kurtulursunuz.
- Tüm alt klasörlerdeki dosyalar otomatik taranır.

------------------------------------------------------------
👥 KİMLER KULLANMALI?
------------------------------------------------------------
- 🖥️ **Web tasarımcılar:** WebP formatındaki görselleri düzenlemek isteyenler.
- 📰 **Blog yazarları ve içerik üreticileri:** PNG formatına ihtiyaç duyanlar.
- 🎨 **Grafik tasarımcılar:** PNG olarak düzenleme yapmak isteyenler.
- 💻 **Geliştiriciler:** Projelerindeki WebP görselleri hızlıca dönüştürmek isteyenler.

------------------------------------------------------------
📦 GEREKSİNİMLER
------------------------------------------------------------
Bu script'i çalıştırmak için aşağıdaki Python kütüphanesine ihtiyacınız var:

> Pillow kütüphanesini yüklemek için:
pip install pillow

------------------------------------------------------------
🚀 NASIL KULLANILIR?
------------------------------------------------------------
1️⃣ Script'i bilgisayarınıza indirin veya kopyalayın.
2️⃣ WebP dosyalarının bulunduğu klasöre script'i koyun.  
3️⃣ Terminal veya komut satırında şu komutu çalıştırın:

python convert_webp_to_png.py

💡 İpucu: Script'i, dönüştürmek istediğiniz WebP dosyalarının olduğu klasörde çalıştırın.

------------------------------------------------------------
🗂️ ÖRNEK KLASÖR YAPISI
------------------------------------------------------------
📂 Resimler
 ┣ 📂 AltKlasor1
 ┃ ┗ 📜 foto1.webp
 ┣ 📂 AltKlasor2
 ┃ ┗ 📜 foto2.webp
 ┗ 📜 foto3.webp

Çalıştırdıktan sonra:

📂 Resimler
 ┣ 📂 AltKlasor1
 ┃ ┣ 📜 foto1.webp
 ┃ ┗ 📜 foto1.png
 ┣ 📂 AltKlasor2
 ┃ ┣ 📜 foto2.webp
 ┃ ┗ 📜 foto2.png
 ┣ 📜 foto3.webp
 ┗ 📜 foto3.png

------------------------------------------------------------
⚙️ TEKNİK DETAYLAR
------------------------------------------------------------
- WebP dosyaları **RGBA** formatında açılır ve PNG olarak kaydedilir.
- Aynı isimde PNG dosyası varsa üzerine yazmaz, `(1)`, `(2)` gibi numaralandırır.
- Tüm alt klasörleri otomatik olarak tarar.

------------------------------------------------------------
📝 LİSANS
------------------------------------------------------------
Bu proje **MIT Lisansı** ile lisanslanmıştır.

------------------------------------------------------------
⭐ DESTEK
------------------------------------------------------------
Bu proje işinize yaradıysa, ⭐ vererek destek olabilirsiniz!  
Teşekkürler 🙏
