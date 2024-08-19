# Global_AI_Hub_Repo

# Tas-Kagit-Makas Oyunu

Bu Python reposu ile, kullanıcı ile bir bilgisayar (-robot diye isimlendirildi oyunda-) arasında Taş-Kağıt-Makas oyunu oynanmaktadir. Oyunda, turlar boyunca 2 galibiyet elde eden oyuncu oyunu kazanir. Her aşamada bilgiler ekrana yazdirilir.

1. **Giris:**
   - Fonksiyon, kullanicinin oyuna hazır olup olmadigini sorar. Kullanici 'E' (Evet) veya 'H' (Hayır)'a basarak yanit verir.
   - Eğer kullanıcı 10 defadan fazla 'H' seçerse, oyun otomatik olarak başlatılır.

2. **Oyun Icerigi:**
   - Kullanıcıdan Tas, Kagit veya Makas seçeneklerinden birini seçmesi istenir.  (1: Taş, 2: Kağıt, 3: Makas).
   - Bilgisayar da 1 ile 3 arasinda rastgele (random) bir sayi üretir.

3. **Sonuc:**
   - Kullanicinin ve bilgisayarin secimlerine gore kazanan belirlenir.Her turda kazanan, kaybeden ve berabere durumu ekrana yazdirilir.
   - Toplamda iki tur kazanan ilk oyuncu oyunu kazanir.

5. **Tekrar Oynama:**
   - Oyun sonunda kullaniciya tekrar oynamak isteyip istemedigi sorulur.Kullanici 'E' (Evet)'i secerse oyun tekrar baslar. 'H' (Hayır) secerse oyun sona erer.

## Fonksiyon Aciklamasi

- `isReady()`fonksiyonu kullanicinin oyuna hazır olup olmadığını kontrol eder 
- `tas_kagit_makas_USER()`: Kullanicinin Tas, Kagit veya Makas secimlerini alir ve gecerli bir seçenek mi kontrolu saglanir.
- `tas_kagit_makas_match()`: Oyunun ana fonksiyonu seklinde düsünülebilir.

