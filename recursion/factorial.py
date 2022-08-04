# m!=m⋅(m−1)⋅(m−2)⋅(m−3)...3⋅2⋅1 

def factorial(value):
    if value == 1:
        return value
    else:
        return value*factorial(value - 1)

print(factorial(6))
