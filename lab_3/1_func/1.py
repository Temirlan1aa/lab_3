def gram_to_ounce(grams):
    return grams * 28.3495231 

grams = int(input("Enter how many grams do you have: "))

print(gram_to_ounce(grams), "ounces")


""""
1. A recipe you are reading states how many grams you need for the ingredient.
Unfortunately, your store only sells items in ounces.
Create a function to convert grams to ounces. 
`ounces = 28.3495231 * grams`
"""