def fibonacci(baslangic, bitis):
    #Başlangıç değerlerini belirleme
    a, b = 0, 1
    
    #Başlangıç değerine kadar diziyi ilerletme
    while a<baslangic:
        a, b = b, a+b
    
    #Fibonacci sayılarını yazdırma
    while a<=bitis:
        print(a)
        a, b = b, a+b
        
def main():
    print("Hoşgeldin!\n")
    
    #Kullanıcadan değerleri alma
    baslangic = int(input("Lutfen baslangic degerini giriniz: "))
    bitis = int(input("Lutfen bitis degerini giriniz: "))
    
    #Fibonacci sayı dizisini yazdırma
    fibonacci(baslangic, bitis)
    
main()
