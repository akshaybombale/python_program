# lambda function
x = lambda p, q : p * q
print(x(5, 6))

# normal function
def cube(x):
    return x * x *x

print(cube(2)) 

# map in python
x = [5,8,5,3,1,6,8,6]
new_x = tuple (map(cube ,x))
print(new_x)

# filter in python
def above(a):
    return a>7

new_list= list(filter(above, x))
print(new_list)
    
    