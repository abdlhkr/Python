# list comprehension is an easier way to create lişst from an existing one
""" liste = []
for i in range(5):
    liste.append(i) """
    
# BOTH OF THESE THİNKS MAKE THE SAME THİNG    

new_list = [item for item in range(5)]
print(new_list)

kurum = "BTK akademi"

string_list = [letter.upper() for letter in kurum]
print(string_list)

odd_numbers = [item for item in range(10) if item % 2 == 1]
print(odd_numbers)

odd_and_even_numbers = [item if item % 2 == 1 else "even number" for item in range(10)]
print(odd_and_even_numbers)
# the code above take the odd numbers and if its even it print even number
products_prices = [1000,2000,0,3000,4000]
total_price = [item * 1.18 if item > 0 else "price is weird" for item in products_prices]
print(total_price)


#  1- (1-100) arasındaki sayılardan 12' e tam bölünebilen sayı listesini oluşturunuz.

numbers = [item for item in range(101) if item % 12 == 0]
print(numbers)

# 2- Verilen text içerisindeki rakamları içeren bir liste oluşturunuz.
# text "
text = "Hello 12345 World"
number_list = [int(item) for item in text if item.isdigit()]
print(number_list)

# 3- Sicakliklar listesinde bulunan her hava sıcaklık bilgisine göre 4 derecenin altında buzlanma tehlikesi yazınız.
tempretures = [20,15,0,-5,-2]
is_it_dangereus = [item if item > 4 else "ice danereus" for  item in tempretures]
print(is_it_dangereus)

# 4- ogrenciler ve notlar listelerindeki notu 50 den fazla olan kişileri ekrana dict verisinde yazdırınız.
ogrenciler = ["ali","ahmet","canan"]
notlar = [50,60,80]

info_tuple = [(ogrenciler[i],notlar[i]) for i in range(len(ogrenciler)) if notlar[i] > 50]
print(info_tuple)

info_dict = {ogrenciler[i] : notlar[i] for i in range(len(ogrenciler)) if notlar[i] > 50}
print(info_dict)

nested_list = [(x,y) for x in range(5) for y in range(3)]
print(nested_list)