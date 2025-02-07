size = int (input("Size of array: "))

list = []

for i in range(size):
    num=int(input())
    list.append(num)


def boolean(size):
    a=0
    for i in range(size -1):
        if list[i]==list[i+1]==3:
            a += 1
            break
    if a==1:
        return True
    else:
        return False

print(boolean(size))