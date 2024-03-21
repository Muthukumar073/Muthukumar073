
def iseven(n):
    return(n&1)
n=int(input("Enter the number :"))
if iseven(n)==0:
    print("even")
else:
    print("odd")
