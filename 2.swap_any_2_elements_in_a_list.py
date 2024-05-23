#approach:2         using pop()
mylist=[12,47,89,23,67]
pos1,pos2=1,3
first=mylist.pop(pos1)          #12 (47)            0 1
second=mylist.pop(pos2-1)           #12 89 23 (67)      0 1 2 3
mylist.insert(pos1,second)
mylist.insert(pos2,first)
print(mylist)