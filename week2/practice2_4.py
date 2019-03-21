# smallest 함수를 조건문을 사용하지 않고 smaller 함수만 호출하여 다음 뼈대코드에 맞추어 작성하시오.

def smaller(x,y):
    return min(int(x), int(y))

def smallest(x,y,z):
    return smaller(smaller(int(x), int(y)), int(z))

print(smallest(3,5,9)) # returns 3
print(smallest(5,3,9)) # returns 3
print(smallest(5,9,3)) # returns 3
print(smallest(3,9,5)) # returns 3
print(smallest(9,3,5)) # returns 3
print(smallest(9,5,3)) # returns 3
print(smallest(3,3,5)) # returns 3
print(smallest(5,3,3)) # returns 3
print(smallest(3,5,3)) # returns 3
print(smallest(3,3,3)) # returns 3