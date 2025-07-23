season = input('Please input the season(only winter or summer): ')
temperature = int(input('Please input current temperature: '))

if season == 'winter' :
    if temperature <10 :
        print('Too cold,I will turn on the heating.')

if season == 'summer' :
    if temperature >27 :
        print('Too hot,I will turn on the lowering.')