import time
def how_much_time_does_it_take(fn):
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"{fn.__name__} metodu çalışıyor")
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time -start_time
        print(f"gecen sure : {run_time}")
        return result
    return inner 
#burda içi içe kullanma sebebimiz ikisinede farklı parametler gönderebiliyor olmamız sanırım        
        
        
@how_much_time_does_it_take
def sum_generator():
    return sum((x for x in range(1000)))

@how_much_time_does_it_take
def sum_list():
    return sum([x for x in range(1000)])

generator_list = sum_generator()

sum_list_instance = sum_list()