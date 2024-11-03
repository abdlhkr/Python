import time
import threading
def calculate_square(numbers):
    for i in numbers:
        time.sleep(0.3)
        print(f"karesi : {i**2}")
        
def calculate_cube(numbers):
    for i in numbers:
        time.sleep(0.3)
        print(f"kübü : {i**3}")        

start_time = time.time()
numbers = [1,3,4,6,7,8,9,32,65,98]
thread_1 = threading.Thread(target=calculate_square,args=(numbers,))# args ta tuple bekliyor ondan , var
thread_2 = threading.Thread(target=calculate_cube,args=(numbers,))# args ta tuple bekliyor ondan , var
thread_1.start()
thread_2.start()
""" calculate_square(numbers)        
calculate_cube(numbers) """
thread_1.join()
thread_2.join()
print(f"it takes {time.time()-start_time} second")

# without multi therading it takes : 6.014974117279053 second         
# with multi therading it takes : 0.0006482601165771484 second
# real time :  with multi therading it takes 3.0059828758239746 second almost half of the time
# bu aslında gerçek süre değil her ne kadar ben iki thread oluşturmuş olsamda aslında main thread yani asıl kodu çalıştıran ekstra thread yoluna devam ediyor yani ben iki thread oluşturduğum zaman toplamda çalışan 3 thread oluyor  joın işlemiyle bu sorunu çözeceğim
"""
Thread'lerde "join" işlemi, bir thread'in (iş parçacığının) tamamlanmasını beklemek için kullanılır. Python gibi dillerde, çoklu iş parçacığı (threading) kullanırken, bir ana iş parçacığı diğer iş parçacıklarının tamamlanmasını beklemek istediğinde join() metodunu çağırır.

Örneğin, bir ana iş parçacığı birkaç paralel iş parçacığını başlatabilir. Eğer ana iş parçacığı bu iş parçacıklarının tamamlanmasını beklemeden işlemeye devam ederse, iş parçacıkları arka planda çalışmaya devam eder ve bu da senkronizasyon problemlerine yol açabilir. Bu durumda, join() kullanılarak ana iş parçacığı, diğer iş parçacıklarının tamamlanmasını bekleyebilir. """
