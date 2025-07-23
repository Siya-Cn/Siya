
def check_perfect_number(number):
    dividers = []
    for value in range(1,number):
        if number%value == 0 :
            dividers.append(value)
    if sum(dividers) == number:
        return True
    else:
        return False

for index in range(1,5000):
    if check_perfect_number(index) == True:
        print(index)