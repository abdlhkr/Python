import json
data =  {
         "1" : {
        "title" : "Mack",
        "price" : 80000
    },
        "2" : {
        "title" : "M3 Mackbook Ultra",
        "price" : 999999
    }
   }

    
# bunun iyi yanı ekleme silme arama işlemleri     
with open("product_dict.json") as file:
    data = json.load(file) 
print(data["1"])       
data.update({
    "3": {
        "title" : "çay",
        "price" : 15
    }
})

with open("product_dict.json","w",encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False,indent=4)
# burda lişste olarak aşağıda dict yaptım 

