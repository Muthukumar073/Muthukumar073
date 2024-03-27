a=int(input("Enter the A value:"))
b=int(input("Enter the B value:"))
c=int(input("Enter the C value:"))
x=b*b-4*a*c
deno=2*a
if x>0:
    print("Real Roots")
    root1=(-b+x**0.5)/deno
    root2=(-b-x**0.5)/deno
    print(root1,'and',root2)
elif x==0:
    print("Equal Roots")
    root1=-b/deno
    print(root1)
else:
    print("Imaginary roots")

