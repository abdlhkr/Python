import sys
# 1 - sonsuz aralığında kareleri gösteren fonksiyon
def sayi_uret():
    counter = 0
    while True:
        yield counter ** 2
        counter += 1
    # normalde counter sonsuza giderken sonsuz döngü olur durur generator da öyle bi sorun yok

generator = sayi_uret()
print(next(generator))        
print(next(generator))        
print(next(generator))        
print(next(generator))

# sonsuz döngü olmasına rağmen hata vermiyor pek hoş değil ::((
""" for i in generator:
    print(i)         """
    
    
# fibonacci dizisini önce normal sonra generator ile üret
# ilk n terim diyeim 
def fibonacci(first_n_item : int):
    fibonacci_numbers = [1,1]
    for item in range(first_n_item - 2):    
        last_index = len(fibonacci_numbers) - 1
        next_value = fibonacci_numbers[last_index] + fibonacci_numbers[last_index-1]
        fibonacci_numbers.append(next_value)
    return fibonacci_numbers

result = fibonacci(20)
print(result)    

# generator not only works faster also doesnt require any space even 9000 item
def fibonacci_generator(max):
    a = 0 
    b = 1
    count = 0
    # 1 1 2 3 5 8
    yield 1 
    while count <= max:
        a , b = b , a + b
        yield b
        count += 1
        
        
generator = fibonacci_generator(9000)
""" for i in generator:
    print(i)      """   
    
liste  = [i for i in range(1000)]
generator = (i for i in range(1000))    
# lets see the size difference between them
print(f" list size : {sys.getsizeof(liste)} \n generator size : {sys.getsizeof(generator)} ")
"""  list size : 8856 
 generator size : 192  
 thats for 1000 item imagine about millions ::(("""



