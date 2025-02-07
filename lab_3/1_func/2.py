"""
2. Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion:
`C = (5 / 9) * (F – 32)`
"""

def f_to_c(F):
    minus = F - 32
    c = (5 / 9) * (minus)
    return c

num = int(input("Enter temperature: "))

print(f_to_c(num))