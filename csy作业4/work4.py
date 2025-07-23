#integer = list(range(1,))
#number_list = []

#对于质数的条件限定有点问题 但实在想不出如何限定质数了
'''
def function(integer,number_list):
    for one_integer in integer :
        while one_integer%2 ==1 :
             number_list.append(one_integer)
             print(number_list)
             if len(number_list) <=200 :
                 break
 '''                
             
#function(integer,number_list)

def get_prime_number(number):
    for value in range(1,number):
        if number == 1:
            return True
        if number ==2:
            return True
        if number%value ==0 :
            return False
        
get_prime_number(1)

