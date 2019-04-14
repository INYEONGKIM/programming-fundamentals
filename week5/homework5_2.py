def binSearchClosest(list, key):
    if list==[]:
        return None
    elif len(list)==1:
        return 0
    left=0; right=len(list)-1

    # binary search
    while left<right:
        mid = (left + right) // 2
        if list[mid]==key:  # found
            return mid
        elif list[mid]>key:
            right=mid-1
        else:
            left=mid+1


    # left==right
    if left<=0: return 0
    if left>=len(list)-1: return len(list)-1
    if key > list[left]:
        if abs(list[left] - key) <= abs(list[left + 1] - key):
            return left
        else:
            return left + 1
    else:
        if abs(list[left-1] - key) <= abs(list[left]-key):
            return left-1
        else:
            return left

    # if left>right:
    #     if abs(list[right]-key)<=abs(list[left]-key):
    #         return right
    #     else:
    #         return left




print(binSearchClosest([],3))   # None
print(binSearchClosest([3],3))  # 0
print(binSearchClosest([1,2,5,7,8],3))  # 1
print(binSearchClosest([1,2,5,7,8],5))  # 2
print(binSearchClosest([1,2,5,7,8],6))  # 2
print(binSearchClosest([1,2,5,9,10],8)) # 3
print(binSearchClosest([1,2,5,9,10],4)) # 2


# while True:
#     n = int(input())
#     print(binSearchClosest([1,2,5,9,10],n))

# import sys
#
# def binSearchClosest(list, key):
#     if list==[]:
#         return None
#     elif len(list)==1:
#         return 0
#     left=0; right=len(list)-1
#
#     # binary search
#     while left<right:
#         mid = (left + right) // 2
#         if list[mid]==key:  # found
#             return mid
#         elif list[mid]>key:
#             right=mid-1
#         else:
#             left=mid+1
#     min=sys.maxsize; idx=-1
#     for i in list:
#         if abs(i-key)<min:
#             min=abs(i-key)
#             idx=list.index(i)
#     return idx