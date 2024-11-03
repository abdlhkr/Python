class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        
# bu objenin iterable olduğunu söylüyoruz        
    def __iter__(self):
        return self
    
# iterator kullanılırken kullanılan metod bu     
    def __next__(self):
        if self.start < self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration            
       
for i in MyNumbers(10,20):
    print(i)        