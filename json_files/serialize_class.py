import json
class Product:
    def __init__(self,productID : int,title : str,price : int):
        self.id = productID
        self.title = title
        self.price = price

# serialize :
    
""" p1 = Product("1","çorba","50")
p2 = Product("2","elma","5")
p3 = Product("3","araba","500000")
p4 = Product("4","ev","50")
p5 = Product("5","uçak","99999999")
product_list = [p1.__dict__,p2.__dict__,p3.__dict__,p4.__dict__,p5.__dict__]
with open("classJson.json","w",encoding="utf-8") as file:
    json.dump(product_list,file,ensure_ascii=False,indent=4)        

# burda liste aşağıda dict hali var 

product_dict = {
    "p1" : p1.__dict__,
    "p2" : p2.__dict__,
    "p3" : p3.__dict__,
    "p4" : p4.__dict__,
    "p5" : p5.__dict__
}    
with open("classJson.json","w",encoding="utf-8") as file:
    json.dump(product_dict,file,ensure_ascii=False,indent=4)       """
    
    
# deserialize : 
    
    
with open("classJson.json") as file:
    product = json.load(file)

print(product)
urunler = []
for key,value in product.items(): 
    urunler.append(Product(key,value["title"],value["price"])) 
    
for p in urunler:
    print(p.title)      