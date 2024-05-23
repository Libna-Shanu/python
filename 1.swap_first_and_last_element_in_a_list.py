#approach:1 
list=[56,89,45,78]
size=len(list)
temp=list[0]
list[0]=list[size-1]
list[size-1]=temp
print(list)