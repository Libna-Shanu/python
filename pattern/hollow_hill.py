n=5
for i in range(n):
    for j in range(i,n):            #decreasing_space
        print(" ",end=" ")
    for j in range(i+1):            #increasing_star
        if(i==n-1 or j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i+1):
        if(i==j or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()