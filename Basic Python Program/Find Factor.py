def factor(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)

num=int(input("Enter the Number:"))
print("The factor of ",num,"is")
factor(num)   
