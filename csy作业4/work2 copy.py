
number = 1
Fibonacci = [1]
while True :
    print(number)
    number = number+number
    Fibonacci.append(number)
    length = len(Fibonacci)
    
    if length == 100:
        break


#好像有点问题 不是斐波那契数列 而是等比数列

'''
def fibonacci(number) :
    if number <= 2 :
        return number 
    result = fibonacci(number-2) + fibonacci(number-1)
    return result

print(fibonacci(7))
'''
         

