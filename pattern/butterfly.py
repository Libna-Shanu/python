n=5
for i in range(n):
    for j in range(i+1):            #increasing_star(i+1)      
            print("*",end="")
    for j in range(i,n):            #decreasing_space(i,n)       
            print(" ",end="")
    for j in range(i,n-1):          #decreasing_space(i,n-1)  
            print(" ",end="")
    for j in range(i+1):            #increasing_star(i+1)     
            print("*",end="")
    print()
for i in range(n):   
    for j in range(i,n):            #decreasing_star(i,n)        
            print("*",end="")
    for j in range(i+1):            #increasing_space(i+1)        
            print(" ",end="")
    for j in range(i):              #increasing_space(i)          
            print(" ",end="")
    for j in range(i,n):            #decreasing_star(i,n)      
            print("*",end="")       
    print()

    