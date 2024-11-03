import time
import multiprocessing

arr = [i for i in range(20)]
def calculate_square(arr,liste):
    global liste_square
    for index,value in enumerate(arr):
        time.sleep(0.3)
        """ print(f"karesi : {i**2}") """
        liste[index] = value ** 2
# enumrate indexi ve indexin içindeki değeri döndürür
def calculate_cube(arr,liste):
    global liste_cube
    for index,value in enumerate(arr):
        time.sleep(0.3)
        """ print(f"kübü : {i**3}") """
        liste[index] = value ** 3   

if __name__ == "__main__":
    # liste tanımlamarını tüm processlerin paylaştığı ortak alana alıyoruz
    liste_square = multiprocessing.Array('i',20)
    liste_cube = multiprocessing.Array('i',20)
    arr = [i for i in range(20)]
    start_time = time.time()
    process1 = multiprocessing.Process(target=calculate_square,args=(arr,liste_square,))
    process2 = multiprocessing.Process(target=calculate_cube,args=(arr,liste_cube,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    # burdaki işlemler multi threading ile aynı nerdeyse ondan açıklama yapmadım 
    print(f"it takes  : {time.time() - start_time}  with multi processing" )
    print(liste_square)
    print(liste_cube)
    for i in liste_square:
        print(i)
    for i in liste_cube:
        print(i)    
    # bunlar ortak alandan geldiği için sorun olmayacak sanırım
    
    
    
    
    # farklı memorylerde yapıldığı için bu ekleme işlemi main memory de değeri görüntüleyemiyor
    # kısaca main memoryde olan listeyi biz boş tamnımladık ama processlerde olan memorylerde doldu orda 
    # çağırırsak dolu olacak gibi düşün 
"""     start_time = time.time()
    calculate_square(arr)
    calculate_cube(arr)    
    print(f"it takes  : {time.time() - start_time}  without multi processing" ) """
    # not multi tasking de farklı memoryler kullanılır bu yüzden birinde üretilen bir değer bir diğerinde kullanılmak istenirse veri paylaşımı yapılması gerekir veri paylaşım işlemleri yavaştır
    # it takes  : 6.080592393875122  with multi processing
    # it takes  : 12.040782928466797  without multi processing
    # what the hell am I goıng all that time ::((

