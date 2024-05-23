#approach:1 

mylist=[56,67,89,40,23]
ele=4
flag=0
for i in mylist:
    if(i==ele):
        flag=1
        print("Element found at index")
        break
    if(flag==0):
        print("Element not found")
