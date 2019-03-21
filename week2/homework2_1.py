def smallerOdd(x,y):
    if x<y:
        return x
    else:
        return y

def smallestOdd(x,y,z):
    x = int(x)
    y = int(y)
    z = int(z)
    if x%2==0 and y%2==0 and z%2==0:
        return None
    else:
        if x%2==1:
            min = x
            if y%2==1:
                min = smallerOdd(min,y)
            if z%2==1:
                min = smallerOdd(min,z)
            return min
        elif y%2==1:
            if z%2==1:
                return smallerOdd(y,z)
            return y
        else:
            return z


print(smallestOdd(3,2,2)) # returns 3
print(smallestOdd(3,5,7)) # returns 3
print(smallestOdd(3,5,1)) # returns 1
print(smallestOdd(8,3,4)) # returns 3
print(smallestOdd(8,3,5)) # returns 3
print(smallestOdd(8,5,3)) # returns 3
print(smallestOdd(2,8,3)) # returns 3
print(smallestOdd(2,8,4)) # returns None
