def square(a):
    return pow(a,2)
print(square(2))

# above and belowe expressions make the same things
kare_al = lambda a: pow(a,2)
print(kare_al(2))

# we can use lambda expressions to create multiple functions

def my_func(n):
    return lambda a: a * n
# we can create function 
multile_by_two = my_func(2)
multile_by_tree = my_func(3)
print(multile_by_two(2),multile_by_tree(3))


