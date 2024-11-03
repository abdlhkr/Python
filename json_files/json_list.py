import json
data = [
    {
        "id" : 1,
        "title" : "Mack",
        "price" : 80000
    },
   {
        "id" : 2,
        "title" : "M3 Mackbook Ultra",
        "price" : 999999
    }
]
""" with open("ders6-json-files/Product_list.json","w") as file:
    json.dump(data,file,indent=4) """
    
# adding an element to a json list ::

new_product = {
        "id" : 3,
        "title" : "poşet",
        "price" : 1
}    

# ekleme yaarken önce oku lsiteye döndür sonra ekle ve geri yaz
with open("ders6-json-files/Product_list.json") as file:
    data = json.load(file)
    data = list(data)
    data.append(new_product)
    with open("ders6-json-files/Product_list.json","w",encoding="utf-8") as added_file:
        json.dump(data,added_file,ensure_ascii=False,indent=4)
    
    