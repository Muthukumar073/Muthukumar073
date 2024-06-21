arr=[7,1,8,4,9,2]
arr1=sorted(arr)

def binarysearch(arr1,tar):
    low ,high=0,len(arr1)-1

    while low <= high:
        mid=(low+high)//2
        if arr1[mid]==tar:
            return mid
        elif arr1[mid]<tar:
            low=mid+1
        else:
            high=mid-1
    return -1

print(binarysearch(arr1,8))





