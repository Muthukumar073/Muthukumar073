str1=input("Enter a String1:")
str2=input("Enter a String2:")
str1=str1.lower()
str2=str2.lower()

if len(str1)==len(str2):
    str_sorted1=sorted(str1)
    str_sorted2=sorted(str2)
    if str_sorted1==str_sorted2:
        print("Anagram")
    else:
        print("NOT a Anagram")
else:
    print("It is Not")
