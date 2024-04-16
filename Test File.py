for i in range(0,10):
    for j in range (0,10):
        if(j==0 or j==9 or i==0 or i==9):
            print("X",end="")
        else:
            print(" ",end="")
    print()    
