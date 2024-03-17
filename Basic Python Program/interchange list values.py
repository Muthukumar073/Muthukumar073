li=[]
n=int(input("Enter the Range :"))
for i in range(0,n):
    ele=int(input())
    li.append(ele)
print("Before Interchange :",li)
li[0],li[4]=li[4],li[0]
print("After Interchange :",li)
