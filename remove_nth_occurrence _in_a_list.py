


mylist=["geeks","for","geeks"]
word="geeks"
N=2
count=0
for i in range(0,len(mylist)):
    if (mylist==word):
        count=count+1
        if(count==N):
            del mylist[i]
print(mylist)
        
