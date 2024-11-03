def n_selamlam(count):# SÜPER HİZANLANMAMIŞ MI AMA ANFNRELSŞGŞ
    def selamlama(fn):# SÜPER HİZANLANMAMIŞ MI AMA ANFNRELSŞGŞ
        def inner(ad):# SÜPER HİZANLANMAMIŞ MI AMA ANFNRELSŞGŞ
            for i in range(count):
                fn(ad)
        return inner
    return selamlama

@n_selamlam(1)
# gunaydın çağrıldığı zaman selamlamaya gundydını referans olarak gönder
def gunaydin(ad):
    print(f"gunaydınnn {ad}")

@n_selamlam(5)
def iyi_gunler(ad):
    print(f"iyi gecelerrr {ad}")
    
gunaydin("ali")
iyi_gunler("sena") 
""" #n kez çalışan selamlama gibi bişey ama n e her seferinde biz karar veriyorz """



import time
def decorator_speed_test(count):
    def how_much_time_does_it_take(fn):
        def inner(*args, **kwargs):
            start_time = time.perf_counter()
            for _ in range(count):
                print(f"{fn.__name__} metodu çalışıyor")
                result = fn(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time -start_time
            print(f"gecen sure : {run_time}")
            return result
        return inner 
    return how_much_time_does_it_take
#burda içi içe kullanma sebebimiz ikisinede farklı parametler gönderebiliyor olmamız sanırım        
        
        
@decorator_speed_test(10)
def sum_generator():
    return sum((x for x in range(1000)))

@decorator_speed_test(10)
def sum_list():
    return sum([x for x in range(1000)])

generator_list = sum_generator()

sum_list_instance = sum_list()