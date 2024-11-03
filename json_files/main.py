#deserialize işlemler 
import json
""" with open("ders6-json-files\Product.json") as file:
    data = file.read()
print(data)     """
# bu şekilde alınan bilgi string formatında oluyor o yüzden deserialize işlemi yapılarak dict e çeviricez
with open("ders6-json-files\Product.json") as file:
    data = json.load(file)
print(data)        
    # load farklı dosyada ise kullanılır loads ise aynı dosyada 3 tırnaklar arasında bilgi varsa kullanılır yani pek kullanılmaz
print(data["title"])

# json string
data =  """
        {
            "id" : 1,
            "title" : "Mackbook pro",
            "rating" : "8.5",
            "price" : 90000,
            "category" : "Bilgisayar",
            "colors" : ["Red","Black"]

        }
"""
data = json.loads(data)
print(data)

# dict veriyi json stringe çevirme dosyaya kaydetmek için 

data = {
            "id" : 1,
            "title" : "Mackbook pro",
            "rating" : "8.5",
            "price" : 90000,
            "category" : "Bilgisayar",
            "colors" : ["Red","Black"]

        }
print(data)
print(type(data))
# class dict
""" data =  json.dumps(data)
print(data)
print(type(data)) """
# class str

with open("ders6-json-files\Product.json","w",encoding="utf-8")  as file:
    json.dump(data,file,indent=4) # ne yazılıcak , nereye yazılıcak