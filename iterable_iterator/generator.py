def counter(max : int):
    counter = 1
    numbers = []
    
    while counter < max:
        yield counter
        counter += 1
        
        # bu veri akışı oluşturur bellekte yer kaplamaz 
        # generator içerisinde iter ve next metodunuda barındırır yani iterable bi nesne oluşturur
        # bu objeyi for ile otomatik iterate ederek üstünde gezinilebilir
    
    
    
    
"""     while counter < max:
        numbers.append(counter)
        counter += 1
                # bu işlem kısa 100 , 2000 gibi sayılarda sorun çıkarmazken daha büyük boyutlu dizilerde oldukça alan kaplar
    return numbers """


generator = counter(10)  
""" 
next(generator)
next(generator)
next(generator)
print(dir(generator))
for item in generator:
    print(item) """
# burda dikkat edilmesi gereken nokta generatorun kullanımı ointer gibi denilebilir next ile iler gidildikten sonra geri dönüş yok bu bakımdan tek yönlü linked list ile benzetilebilir generator hadızada tutlan bi listeye aşağıdaki şeklide dönüştürülebilir
sonuc =list(generator)
print(sonuc)

# ONEMLİ list comrehensionda köşeli yerine normal parantez kullanırsan liste yerine generator döner

liste = (i for i in range(10))
while True:
    try:
        print(next(liste))
    except StopIteration:
        break










