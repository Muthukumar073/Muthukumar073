num=int(input("Enter a Number:"))
m =list(map(lambda x:2**x, range(num)))
for i in range(num):
    print("2 raised to power",i,"is",m[i])
