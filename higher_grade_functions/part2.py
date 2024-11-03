def filter(fn,liste : list):
    reuslt = []
    for i in liste:
        if fn(i):
            reuslt.append(i)
    return reuslt
def is_even(number):
    return number % 2 == 0

def is_positive(number):
    return number > 0 

numbers = [1,2,3,5,7,9,34,99,100]
even_result = filter(is_even,numbers)
positive_result = filter(is_positive,numbers)
print(even_result)
print(positive_result)
# bi fonsiyomu başka bir fonksiyona girdi olarak girerken parantez () kullanılmaz

def selamlama(fn):
    def inner(ad):
        print("hos geldiniz")
        fn(ad)
        print("hoşcakalın")         
    
    return inner

@selamlama
# gunaydın çağrıldığı zaman selamlamaya gundydını referans olarak gönder
def gunaydin(ad):
    print(f"gunaydınnn {ad}")

@selamlama    
def iyi_gunler(ad):
    print(f"iyi gecelerrr {ad}")
    


""" gunaydin_text = selamlama(gunaydin)
iyi_gunler_text = selamlama(iyi_gunler)
gunaydin_text()
print("\n\n\n")
iyi_gunler_text() """

# şimdi gelelim decorator fonk burda ne işe yarıyor eğer iyi gunler ve gunaydinda @ dekore edicek fonk adı yazarsakkk yukardaki gibi yapmıyoruz daha kolay oluyor öyle yani
        
gunaydin("ali")
print("\n\n\n")
iyi_gunler("orhan")        


""" def iki_kere_calis(fn):
    def inner(*args, **kwargs):
        fn(*args, **kwargs)
        fn(*args, **kwargs)
    return inner    """
def iki_kere_calis(fn):
    def inner(*args, **kwargs):
        fn(*args, **kwargs)
        return fn(*args, **kwargs)
    return inner   

#selamda ad olmasına rağmen merhaba da yok bu durumu çözmek için kwargs ve args kullanılır
@iki_kere_calis
def merhaba():
    print("merhaba ")
    
@iki_kere_calis
def selam(ad):
    print("selam ",ad)    
    
@iki_kere_calis    
def iyi_gunler():
    return "iyi gunler"    
   
selam("ali")
merhaba()
""" print(iyi_gunler())  # bunun none dönme sebebi inner fonk çağrılması ve onun bi değer döndürmemesi
şimdi bu sorunu çözmek için yukarıdaki iki kere çalış fonk düzenleyelim """
print(iyi_gunler())