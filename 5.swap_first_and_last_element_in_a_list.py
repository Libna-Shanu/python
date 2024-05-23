#approach:5 using pop() function
list=[18,59,2,5,7,2,6]
first=list.pop(0)
last=list.pop(-1)
list.insert(0,last)
list.append(first)
print(list)