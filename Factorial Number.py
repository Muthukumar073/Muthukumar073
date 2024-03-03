Factorial Number
def fact(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x*fact(x-1)

num=int(input("Enter a Number :"))
print(f"The Factorial of {num} is {fact(num)}")
