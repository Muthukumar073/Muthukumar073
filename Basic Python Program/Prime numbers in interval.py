def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,end=" ")
            
number1=int(input("Enter the starting Range: "))
number2=int(input("Enter the ending Range: "))
print(f"The prime Numbers between {number1} and {number2} are:")
for i in range(number1,number2+1):
    prime(i)
