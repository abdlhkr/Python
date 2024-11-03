# all = and  any = or oerator
# And => True and True => all()
# Or => True or False => any()

sonuc = all([True,True,True])
print(f"sonuc 1 : {sonuc}")
sonuc = all([True,True,False])
print(f"sonuc 2 : {sonuc}")
sonuc = any([True,True,True])
print(f"sonuc 3 : {sonuc}")
sonuc = any([True,True,False])
print(f"sonuc 4 : {sonuc}")
# all the user names starts with an a ? 
users = ["ali","ahmet","oğuz"]
results = [user[0] == "a" for user in users]
print(results)
print(all(results))
# is there anyone who's name not start with an a
print(any(results))