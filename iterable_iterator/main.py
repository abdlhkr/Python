# iterable
# iterator
numbers = [1,2,3,4,5,6]
# burdaki liste iterable oluyor yani üstünde döngü kurabiliyoruz
""" for i in numbers:
    print(i) """
# numbers iterable bi nesne bu nesnenin de bi iterator olması gerek bunu for otomatik yapıyor    
    
    
    
print(dir(numbers))  # __iter__ metodu iterable olmasını sağlayan metod
# next metodu sırayla ilk ikinci elemanı döndürür ama iterator stünde çalışır 
# Return the next item from the iterator. şimdi listemiz iterable bunu nasıl iterator 
# haline getiririrz ?
iterator = iter(numbers)
""" print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) """
# if you try to use next method on numbers : TypeError: 'list' object is not an iterator
""" print(next(numbers)) """

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break