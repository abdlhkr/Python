users = [
    {"username":"abdullah","posts":["post 1","post 2","post 3"], "email" :"sanane@gmail.com"}, 
    {"username":"ali","posts":["post 1"], "email" :"sanane@gmail.com"}, 
    {"username":"murat","posts":["post 1","post 2"], "email" :"sanane@gmail.com"} 
]

# sort by their names

result = sorted(users,key=lambda a: a["username"])
result_names = [name["username"] for name in result]
print(result_names)

# who sent the most post

result = sorted(users,reverse=True,key=lambda user: len(user["posts"]))
result_names = [name["username"] for name in result]
print(result_names)