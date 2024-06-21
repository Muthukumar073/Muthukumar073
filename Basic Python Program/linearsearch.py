def linear(value,tar):
    for i in range(len(value)):
        if value[i]==tar:
            return tar
    return -1

value=[2,4,6,1,9,3]
tar=4
print(linear(value,tar))