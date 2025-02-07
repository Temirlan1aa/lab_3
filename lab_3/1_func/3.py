"""
3. Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
`create function: solve(numheads, numlegs):`
"""


legs = 94
heads = 35

def num_of_chickens(legs , heads):
    if legs <= heads * 2:
        return legs//2
    else:
        return heads

def num_of_rabbits(legs , heads):
    if legs <= heads * 4:
        return legs//4
    else:
        return heads
    
print("number of chickens ", num_of_chickens(legs, heads))

print("number of rabbits ", num_of_rabbits(legs, heads))