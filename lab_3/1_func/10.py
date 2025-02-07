def unique_elements(lst):
    list2 = []
    for item in lst:
        if item not in list2:
            list2.append(item)
    return list2

list1 = []

size = int(input('size:'))

for i in range(size):
    num = int(input())
    list1.append(num)

print(unique_elements(list1))