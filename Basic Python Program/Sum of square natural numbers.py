def square(n):
    sum=0
    for i in range(1,n+1):
        sum+=(i*i)
    return sum    
num=int(input("Enter a Number:"))
print(square(num))
