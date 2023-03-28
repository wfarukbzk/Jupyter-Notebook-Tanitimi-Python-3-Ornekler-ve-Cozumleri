def mukemmel(sayi):
    #Pozitif tam bolenleri hesaplamak için değişken oluşturma
    toplam = 0
    
    #Bölenleri kontrol etme ve toplam değerini güncelleme
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
            
    #Toplam değerinin sayıya eşit olup olmadığını kontrol etme
    if toplam == sayi:
        return True
    else:
        return False
    
def main():
    print("Hoşgeldiniz!\n")
    
    #Kullanıcıdan değer alma
    sayi = int(input("Lutfen bir sayi girin: "))
    
    mukemmel(sayi)
    
    #Sayının mükemmel olup olmadığını ekrana yazdırma
    if mukemmel(sayi):
        print(sayi, "bir mukemmel sayidir!")
    else:
        print(sayi, "bir mukemmel sayi degildir!")
        
main()
