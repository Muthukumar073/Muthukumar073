def ascii(char):
    return ord(char)

char=input("Enter the Character:")
if len(char)==1:
    print(f"The ASCII value of {char} is {ascii(char)}")
else:
    print("It is Invalid")
