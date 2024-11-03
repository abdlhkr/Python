numbers = [1,2,3,4,5]
square = lambda a: pow(a,2)


result_object = map(square,numbers) 
print(result_object)
# map function takes two input function and an iterable 
# it return an object of a list

actual_result = list(result_object)
print(actual_result)

string_numbers = ["1","2","3","4","5"]
numbers = list(map(int,string_numbers))
print(numbers)


# like map function filter takes two input one function wich returns T/F and an iterable
""" def negative_numbers(a):
    return a < 0 """

negative_numbers = lambda a: a < 0
numbers = [1,3,8,9,-9,-5,-2] 
result = list(filter(negative_numbers,numbers))
print(result)

users = [
    {"username" : "sadik turan", "posts" : ["post 1"]},
    {"username" : "ali turan", "posts" : ["post 1", "post  2"]},
    {"username" : "ayşe turan", "posts" : ["post 1", "post  2"]}
]

# users who has at least two post

filter_results = list(filter(lambda a: len(a["posts"]) > 1, users))
filter_names = [item["username"] for item in filter_results]
print(filter_results)
print(filter_names)