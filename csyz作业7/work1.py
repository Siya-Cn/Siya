def weight_lifting(sex,weight):
    if sex == 'male':
        if weight >= 54 :
            print('您已获得男子组参赛资格！')
    elif sex == 'fwmale' :
        if weight >= 46 :
            print('您已获得女子组参赛资格！')
    else:
        print('性别异常！！！')


