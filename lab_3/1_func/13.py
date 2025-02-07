import random

def guess_number(rand_num , guesses):



    num = int(input("Take a guess.\n"))

    if rand_num > num :
        guesses+=1
        print("Your guess is too low.")
        guess_number(rand_num , guesses)

    elif rand_num < num:
        guesses+=1
        print("Your guess is too high.")
        guess_number(rand_num , guesses)

    else:
        guesses+=1
        print(f"Good job, {name}! You guessed my number in {guesses} guesses!")



name = input("Hello! What is your name?\n")

print(f"Well, {name}, I am thinking of a number between 1 and 20\n")

rand_num = random.randint(1 , 20)

guess_number(rand_num , 0)