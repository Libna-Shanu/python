arr=[12,45,78,92,58,29]
max=arr[0]
size=len(arr)
for i in range (size):
    if arr[i]>max:
        max=arr[i]
print(max)