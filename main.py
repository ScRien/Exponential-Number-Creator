print("Üslü Sayı Oluşturma | Hoşgeldin!")

while True:
    Us = int(input("\nÜs'ü Giriniz: "))
    Taban = int(input("\nTaban'ı Giriniz: "))
    kontrol = input("\nNot: Çıkmak için 'Q', devam etmek için '1' yazınız: ")
    if kontrol == "Q":
        print("Çıkış Yapıldı!")
        break
    if kontrol == "1":
        print("\nSonucunuz: ", Us ** Taban)