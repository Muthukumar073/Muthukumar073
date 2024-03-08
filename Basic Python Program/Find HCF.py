def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hc=i
    return hc

num1=int(input("Enter the Number:"))
num2=int(input("Enter the Number:"))
print("The HCF Value is :",hcf(num1,num2))
