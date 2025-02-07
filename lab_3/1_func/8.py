def spy_game(numbers):

    sequence = [0, 0, 7]
    index = 0

    for num in numbers:
        if num == sequence[index]:
            index += 1
            if index == len(sequence):
                return True

    return False


size = int(input())

numbers = []

for i in range(size):
    num = int(input())
    numbers.append(num)

print(spy_game(numbers))