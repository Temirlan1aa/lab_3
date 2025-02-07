def palindrom(var):
    bool = True
    for i in range(len(var)):
            if var[i] == var[len(var)-1-i]:
                bool = True
            else:
                bool = False
                break
    return bool
variable = input()
print(palindrom(variable))