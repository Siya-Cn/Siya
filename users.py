current_users = ['julie','kiki','jack','rose','taylor']
current_users2 = current_users[:]
new_users = ['jack','rose','cindy','lisa','jane']

upper_user_list = []

for user in current_users:
    upper_user_list.append(user.title())
print(upper_user_list)
    
for one_user in new_users:
    if one_user in current_users :
        print(f'Your name {one_user} has been occupied!')
    else:
        print(f'Your name {one_user} has been built successfully!')

for one_user in new_users:
    if one_user in upper_user_list :
        print(f'Your name {one_user} has been occupied!')
    else:
        print(f'Your name {one_user} has been built successfully!')