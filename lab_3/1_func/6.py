txt = input()

list = txt.split()

size = int(len(list))

list.reverse()

def output_of_txt(size):
    i = 0

    new_txt = ''

    while i!=size:
        new_txt = new_txt + list[i] + ' '
        i+=1

    return new_txt

print(output_of_txt(size))