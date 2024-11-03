class MyNumbers:
    def __init__(self,start,end) -> None:
        self.start = start
        self.end = end
        
    def __iter__(self): # this secial method make our object iterable
        return self
        
    def __next__(self):
            # next method simly a way to say how to iterate over our object
            if self.start < self.end:
                x = self.start
                self.start += 1
                return x
            else:
                raise StopIteration
        

# her ne kadar for döngüsü iteratör üzerinde çalışsada nesnenin iterable olması gerek öncelikle
iterator = iter(MyNumbers(1,20)) 
print(iterator)    # <__main__.MyNumbers object at 0x000001786068A390> its an object it doesnt required space like arrays and so
for i in iterator:
    print(i)        
    
# TypeError: 'MyNumbers' object is not iterable cause we havent defined iter method    