import students

total = []

for one_student in students.students_list:
    sum = one_student['course1'] + one_student['course2'] + one_student['course3']
    total.append(sum)
    print(total)
a = max(total)




