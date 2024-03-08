def palin(var):
    ori=str(var)
    rev=ori[::-1]
    if rev==ori:
        print("It is Palindrome")
    else:
        print("It is not a Palindrome")
    
var=input("Enter the Value:")
palin(var)
