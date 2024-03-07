n=int(input("Enter the Number :"))
temp=n
sum=0
order=len(str(n))
while temp>0:
    digit=temp%10
    sum =sum+digit**order
    temp=temp//10
if n==sum:
    print("The Given number is Armstrong")
else:
    print("The Given number is Not an Armstrong")
