n = input("Enter the number of element of list =") 

list = []
for i in range(n+1):
    x = input("Enter the element = ")
    list.append(x)

for j in range(len(list)):
    min_idx = i
    for k in range(i+1, len(list)):
        if list[min_idx] > list[i]:
            min_idx = k
    list[i],list[min_idx] = list[min_idx],list[i]

print("Sorted array ")
for i in  range(len(list)):
    print("%d" %list[i])
