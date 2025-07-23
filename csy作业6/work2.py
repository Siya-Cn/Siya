import students  

def get_average():
    total_age = 0
    total_height = 0
    student_number = len(students.information)

    for one_dict in students.information:     
        total_age += one_dict['age']
        total_height += one_dict['height']
    
    age_average = {total_age}/{student_number}
    height_average = {total_height}/{student_number}

    print(f'平均年龄为：{age_average}')
    print(f'平均身高为：{height_average}')

get_average()


    

