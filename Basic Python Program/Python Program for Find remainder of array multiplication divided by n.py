import array 
arr=array.array("i",[100,25,35,5,10,14])
product=1
len=len(arr)
n=int(input("Enter the divisible Number :"))
for i in range(len):
    product=product*arr[i]
print(product%n)
