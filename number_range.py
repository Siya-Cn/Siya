for numbers in range(1,21):
    print(numbers)

value = list(range(1,1000001))
print(value)
print(max(value))
print(min(value))
print(sum(value))

value2 = list(range(1,20,2))
for one_value in value2:
    print(one_value)

value3 = list(range(3,31,3))
for a_value in value3:
    print(a_value)

value4 = []
for b_value in list(range(1,11)):
    value5 = b_value*b_value*b_value
    print(value5)
    value4.append(value5)
print(value4)
    