numbers = [1,2,3,4,5,6]
print(max(numbers))
print(min(numbers))

# max and min functions work on int float char and string values

letters = ["a","b","c","d"]
print(max(letters))
print(min(letters))

# while using on strings it looks ascii numbers 
names = ["ali","ahmet","Abdullah","abdullah","Burak","burak"]
print(max(names))
print(min(names))

# max and min functions can also take key values like sorted

longest_name = max(names,key=lambda name: len(name))
print(longest_name)

products = [
    {"name" : "samsun s23", "price": 7000},
    {"name" : "samsun s24", "price": 8000},
    {"name" : "samsun s25", "price": 9000}
]

most_expensive = max(products,key=lambda product: product["price"])
print(most_expensive["name"])