def histogtramm(list , size):

    for i in  range(size):
        str=''

        for j in range(list[i]):
            str += "*"
        
        print(str)


size = int(input("size:"))

list = []

for i in range(size):
    num = int(input())
    list.append(num)

histogtramm(list , size)