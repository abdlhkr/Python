""" def greet(name:str):
    return f"hello {name}"
    
print(greet("ali"))
print(greet)# that returns the adress of the function    
    
merhaba = greet #now both merhaba and greet at the same object
print(merhaba)    
print(greet)    

print(merhaba("ali"))
# lets we delete the greet function
del greet
# it still works yani adres duruyor biz adresi tutan greet variable ını sildik gibi düşünebiliriz

print(merhaba("ali")) """


def outer(number : int):
    def inner(number):
        print(number)
    inner(number)

outer(10)

# for now it doesnt makesense we are gonna use it later
def factoriel(number):
    if number < 0:
        raise TypeError("number should be grater then 0 ") 
    def inner_factoriel(number):
        if number <= 1 : 
            return 1
        else:
            return number * inner_factoriel(number -1)
    
    return inner_factoriel(number)    


print(factoriel(5))

# burda ilk fonk innerın adresini döndürdüğü için her seferinde farklı bir fonksiyon oluşturmak gibi düşünebiliriz sanırım 
def us_alma(taban):
    def inner(ust):
        return taban ** ust
    
    return inner
# ilk eleman outera ikinci eleman innera veri olarak gidiyor
print(us_alma(3)(2))

taban = us_alma(5)
# yukarıda 5 in üslerini hesaplayan bir fonk oluşturduk aşağıda ise onu kullanıyoruz gibi düşün
sonuc = taban(2)
sonuc_v2 = taban(3)
print(sonuc)
print(sonuc_v2)



def islem(islem_adi):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam    

    def carp(*args):
        carpim = 1 
        for i in args:
            carpim *= i
        return carpim
    
    if islem_adi == "toplama":
        return toplama
    if islem_adi == "carpma":
        return carp
    
toplama = islem("toplama")
carpma = islem("carpma") 

 
print(toplama(1,2,3,4,5),carpma(5,4,3))
















