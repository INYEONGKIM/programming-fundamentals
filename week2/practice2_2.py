def smaller(x,y):
    x = int(x)
    y = int(y)
    if x < y:
        return x
    else:
        return y

print(smaller(3,5)) # returns 3
print(smaller(5,3)) # returns 3
print(smaller(3,3)) # returns 3