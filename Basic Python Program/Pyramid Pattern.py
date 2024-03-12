n=[[0,0,0,1,0,0,0],
   [0,0,1,1,1,0,0],
   [0,1,1,1,1,1,0],
   [1,1,1,1,1,1,1]]
for i in n:
    for j in i:
        if j == 1:
            print("*",end='')
        else:
            print(" ",end='')
    print('')
