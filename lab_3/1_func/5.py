"""
5. Write a function that accepts string from user and print all permutations of that string.
"""

txt = input()

list = txt.split()

num1=1



size_of_list = len(list)

def permutation(num , num1):
    for i in range(1 , num +1):
        num1 *= i
    return num1



print(permutation(size_of_list , num1))