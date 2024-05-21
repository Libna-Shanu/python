n=5
for i in range(5):
    for j in range(i+1):            #increasing_star(i+1) 
        print("*",end="")
    print()
for i in range(5):
    for j in range(i,n-1):          #decreasing_star(i,n-1)
        print("*",end="")
    print()