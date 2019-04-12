def binSearchClosest(list, key):
    if list==[]:
        return None
    elif len(list)==1:
        return 0
    left=0; right=len(list)-1

    while left<right:
        mid = (left + right) // 2
        if list[mid]==key:
            return mid
        elif list[mid]>key:
            right=mid-1
        else:
            left=mid+1
    if left>len(list)-1:
        return right
    if right<0:
        return left
    if abs(list[left]-key) >= abs(list[right]-key):
        return right
    else:
        return left


# print(binSearchClosest([1,2,5,7,8],5))
# print(binSearchClosest([1,2,5,7,8],6))
# print(binSearchClosest([1,2,5,9,10],8))
