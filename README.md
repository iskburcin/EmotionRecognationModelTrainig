# Duygu Analizi Modeli Eğitimi: Teknik Tanıtım
## Modelin Amacı ve Genel Bilgi
YUZUG uygulaması, cihazın kamerasından kullanıcıların yüz ifadelerinden duygularını algılayıp ("mutlu," "üzgün," ve "öfkeli"), duygu durumlarına uygun aktiviteler önermeyi hedeflemektedir.

### 1. Adım: Projenin Başlatılması
GitHub’daki EmotionRecognitionModelTraining reposunu klonlayıp yerel bir kopya edinin. Ardından, drive linki ndeki veri seti dosyasını indirerek, clone projenin içine yükleyin. Kodlar içerisindeki dosya yollarını vs. güncelleyin.

### 2. Adım: Veri Ön İşleme
Veri setindeki tüm görüntüler, **recolor_images.py** dosyası kullanılarak gri tonlamaya dönüştürülmüştür. Bu işlem, modelin sadece yapı odaklı öğrenmesini sağlamak içindir. Aynı zamanda **resize_images.py** dosyası ile 224x224 piksel boyutlarına yeniden boyutlandırılıp veri setinde tekrarlanan resimler, **dublican_deleter.py** ile temizlenmiştir.
| Note: Bu aşama ister linkteki veriseti, ister yeni bir veri seti kullanılsın eğer veriler aynı formatta değilse preproceess olarak yapılmalıdır.

### 3. Adım: Modelin Yapılandırılması
Model, klasik bir Convolutional Neural Network (CNN) mimarisi ile oluşturulmuştur (görüntü tabanlı duygu tanıma işlemlerinde etkili ve yaygın bir yöntemdir). -tek tek olgulardan, genel bir çıkarım yapıyor (tümevarım)-. Aşağıda modelin yapısı açıklanmaktadır:
- Conv2D Katmanları: Üç adet Conv2D katmanı, sırasıyla 32, 64 ve 128 filtreli konvolüsyon işlemleri gerçekleştirir. Her biri 3x3 boyutlarında filtrelere sahiptir ve ReLU aktivasyon fonksiyonunu kullanır. Bu katmanlar, modelin yüz ifadelerini tanıması için gerekli olan özellikleri çıkarmasına yardımcı olur. (64 ve 128 filtreleri modelin derinliğini arttırmak için)
- MaxPooling Katmanları: her bir konvolüsyon katmanının ardından MaxPooling katmanı eklenmiştir. Bu, özellik haritalarını (boyut) indirger ve modelin genel performansını artırır.
- Flatten Katmanı: Üçüncü MaxPooling katmanının ardından, özellik haritaları düzleştirilerek tam bağlı katmanlara aktarılır.
- Dense Katmanları: İki adet Dense katmanı bulunur. 256 nöronlu ve ReLU aktivasyon fonksiyonlu katmanın ardından, 3 nöronlu ve softmax aktivasyon fonksiyonu ile nihai duygu sınıflandırması yapılmıştır.

### 4. Adım: Model Eğitimi
Bu süreçte, Adam optimizasyon algoritması ve  compile aşamasında categorical_crossentropy kayıp fonksiyonu kullanılmıştır (modelin hızlı ve etkili bir şekilde öğrenmesini amaçlar). Eğitim sürecinde, modelin performansı her epoch sonunda değerlendirildi:
- Model Doğruluğu (Accurasy): modelin başarımı
- Model Kayıp (Loss): modelin kayıp fonksiyon değerleri
####Bizim en başarılı eğitim sonucumuz:
Model, 32 batch’de, 70 epoch boyunca eğitilmiştir. Grafikte doğruluğun sık dalgalanmaları ve kayıp değerlerinin açık ara artışı overfitting belirtisidir.
![model_output](https://github.com/user-attachments/assets/953729bf-0bf6-48ca-b22d-130ba0399172)

### 5. Adım: Modelin Kaydedilmesi
Eğitim süreci sonunda, modelin farklı formatlarda (.keras, .h5, .json, .tflite) kaydedilmesi gereklidir. Bu sayede, modelin yeniden yüklenmesi ve başka platformlarda (mobil uygulamalarda vs.) kullanılması kolaylaşır.
Modelin **ağırlıkları**, HDF5 (.h5) formatında kaydedilir. Bu, modelin tekrar eğitilmesine gerek kalmadan yüklenebilmesini sağlar.
Modelin **yapısı** JSON formatında kaydedilmiştir. Bu format, modelin sadece mimarisini saklar.
Model ayrıca TensorFlow Lite (TFLite) formatına dönüştürülmüştür (modeli mobil cihazlarda kullanmak için). Ancak, TFLite modelinin performansı, keras modeline göre biraz daha düşüktür.

### 6. Adım: Modelin Test Edilmesi
Modelin performansı, hem gerçek zamanlı (webcam) testler (test_real_time.ipynb) hem de statik görüntü testleri (test_static.ipynb) ile değerlendirilmiştir ve ihtiyaç halinde doğru dosya yoları ile değerlendirilebilir. Farklı formatlardaki modellerin performansları karşılaştırılmış ve en iyi sonuçları elde etmek için çeşitli optimizasyonlar yapılmıştır. 
Test aşamasında Flask kullanılarak bir model çalıştırma denemesi yapılmıştır ancak bu aşama tam anlamıyla başarılı sayılmamaktadır. Flask üzerinde canlı video akışını çalıştırmak mümkün olmamıştır; sadece kayıtlı fotoğraflar üzerinde çalışmıştır. Gelişime açıktır, fakat geleneksel yöntemlerin dışına çıkılmalı, çözümü orada bulamadık :/
