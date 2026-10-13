### return , *arg , **arg lambda

def add(*a): ## *a is a tuple of values and its a data structure in python
    total = 0
    for value in a:
        total = total + value ## 0 + 1 = 1 , 1 + 2 = 3 
    return total

print(add(1,2,3,4))

