# **Diskort**

Diskort, basit bir sohbet ve mesajlaşma uygulamasıdır. Python ile geliştirilmiş bu uygulama, PyQt5 tabanlı bir GUI (Grafiksel Kullanıcı Arayüzü) ve bir istemci-sunucu mimarisine sahiptir. Uygulama, hem genel mesajlaşma hem de özel mesajlaşma özelliklerini destekler.

---

## **Özellikler**
- **Kullanıcı Girişi:** Kullanıcıların bir takma ad (nickname) ile giriş yapmasını sağlar.
- **Genel Sohbet:** Tüm kullanıcılara mesaj gönderme özelliği.
- **Özel Mesajlaşma:** Belirli bir kullanıcıya özel mesaj gönderebilme.
- **Kullanıcı Listesi:** Çevrimiçi olan kullanıcıların listesini görüntüleme.
- **Dinamik Arayüz:** Kullanıcı arayüzü pencere boyutuna göre otomatik olarak yeniden boyutlanır.
- **Kullanıcı Profili Görüntüleme:** Kullanıcıların temel bilgilerini inceleyebilme.
- **Bağlantı Yönetimi:** Sunucuyla olan bağlantının kopması durumunda otomatik olarak hata raporlama.

---

## **Kurulum**

### **Gereksinimler**
- Python 3.9 veya daha yeni bir sürüm
- PyQt5 
- Socket kütüphanesi (standart Python modülü)

### **Adımlar**
1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install pyqt5
   ```
2. **Server.py** dosyasını çalıştırarak sunucuyu başlatın:
   ```bash
   python Server.py
   ```
3. **Diskort.py** dosyasını çalıştırarak istemciyi başlatın:
   ```bash
   python Diskort.py
   ```

---

## **Kullanım**

1. **Server.py** dosyasını çalıştırın. Sunucuya bağlanması gerekmektedir.
2. **Diskort.py** dosyasını çalıştırdığınızda bir giriş ekranı açılır.
3. Takma adınızı girerek "Giriş" butonuna basın.
4. Sohbet penceresi açıldıktan sonra:
   - Mesajlarınızı yazıp "Gönder" butonuna tıklayarak mesaj gönderebilirsiniz.
   - Çevrimiçi kullanıcı listesine sağ tıklayarak özel mesaj gönderebilir veya kullanıcı profillerini görüntüleyebilirsiniz.

---

## **Proje Mimarisi**

### **Server.py**
- Sunucu tarafında kullanıcı bağlantılarını yönetir.
- Gelen mesajları yayınlar (broadcast) veya özel mesajları ilgili kullanıcıya yönlendirir.
- Çevrimiçi kullanıcı listesini düzenli olarak günceller.

### **Diskort.py**
- Kullanıcı arayüzünü sağlar.
- Mesajlaşma, kullanıcı listesi görüntüleme ve özel mesajlaşma özelliklerini içerir.
- Kullanıcı girişini yönetir ve sunucuyla iletişim kurar.


---

## **Ekran Görüntüleri**

### **Giriş Ekranı**
- Kullanıcıdan takma ad alır.
- Basit ve kullanıcı dostu bir tasarım.


### **Sohbet Ekranı**
- Sohbet alanı, çevrimiçi kullanıcı listesi ve mesaj gönderme bölümü içerir.
- Dinamik pencere boyutlandırma.

![TekliEkran](https://github.com/user-attachments/assets/9c09a11f-c719-445e-bada-40a14fc62374)

![ÇokluMesaj](https://github.com/user-attachments/assets/9d32697c-fe66-4a90-909a-46e407985e6f)
---

## **Bilinen Sorunlar**
- Sunucuya bağlanılamadığı durumlarda uygulama otomatik olarak çıkış yapar.
- Aynı kullanıcı adıyla giriş yapılması desteklenmez.

---

## **Katkıda Bulunun**
Projeye katkıda bulunmak isterseniz şu adımları izleyebilirsiniz:
1. Bu projeyi forklayın.
2. Değişikliklerinizi yapın.
3. Pull Request gönderin.

---

## **Lisans**
Bu proje MIT lisansı altındadır. Daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.
