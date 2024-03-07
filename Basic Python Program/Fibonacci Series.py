num=int(input("Enter the Number:"))
n1,n2=0,1
su=0
if num <=0:
    print("Give a number Greater than zero ")
else:
    for i in range(0,num):
        print(su, end=" ")
        n1=n2
        n2=su
        su = n1+n2
    
