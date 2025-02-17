list1 = []
list2 = []

num3 = 0
num4 = int()
print("enter the amount of numbers in the list")
num1 = int(input())

for i in range(num1):
    print("enter the numberes you want to add to the list")
    num2 = int(input())
    list1.append(num2)


#list now contain numbers
num_min = min(list1)

while len(list2) < len(list1):
    
    for i in range(len(list1)):
        if num_min not in list2:
            list2.append(num_min)
            if list1[i] > num_min:
                list2.append(list1[i])
                num4 = list1[i]
        else:
            if list1[i] > num4:
                list2.append(list1[i])
                num5 = list1[i]

print(list1)    
print(list2)

    
        



    


