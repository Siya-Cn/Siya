print('请输入两个数，我会将他们相加')
print('退出请输入“q”')

while True:
    first_number = input('第一个数：')
    if first_number =='q':
        break

    second_number = input('第二个数：')
    if second_number =='q':
        break
    
    answer = first_number + second_number
    print(answer)

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print('您不能输入文字！')
    else:
        print(answer)