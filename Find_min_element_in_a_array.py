arr=[80,58,73,45,90,12,32]
min=arr[0]
for i in range(len(arr)):
    if arr[i]<min:
        min=arr[i]
print(min)