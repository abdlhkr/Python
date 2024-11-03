numbers = [1,2,3,4,5,6,7,8,9,10]
sum_of_ten = sum(numbers)
print(sum_of_ten)

products = [
    {"name" : "samsun s23", "price": 7000},
    {"name" : "samsun s24", "price": 8000},
    {"name" : "samsun s25", "price": 9000}
]

total_price = sum([item["price"] for item in products])
print(total_price)

sonuc = round(1.2)
print(sonuc)
sonuc = round(1.5)
print(sonuc)
sonuc = round(2.6)
print(sonuc)
sonuc = round(1.26,2)
print(sonuc)
sonuc = round(3.6785,3)
print(sonuc)