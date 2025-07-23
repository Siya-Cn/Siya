list = [1,2,3,3,3,3,4,5]

def list_robot(list):
    new_list = []
    for number in list:
        if number not in new_list:
            new_list.append(number)
    
    print(new_list)

list_robot(list)


