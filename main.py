print("Üslü Sayı Oluşturma | Hoşgeldin!")

while True:
    Taban = int(input("\nTaban'ı Giriniz: "))
    Us = int(input("\nÜs'ü Giriniz: "))
    kontrol = input("\nNot: Çıkmak için 'Q', devam etmek için '1' yazınız: ")
    if kontrol == "Q":
        print("Çıkış Yapıldı!")
        break
    if kontrol == "1":
        print("\nSonucunuz: ", Us ** Taban)
