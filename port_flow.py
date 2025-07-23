old =  {"8001":11370, "8002": 15005, "8005": 393922, "8006": 322322, "8007": 23234}
new =  {"8001":13930, "8005": 693922, "8006": 522255, "8007": 66666, "8009": 7777}

result = {}

for key in old.keys():
    if key in new.keys():
        result[key]= new[key]-old[key]

print(result)


'''
new_list = []
old_list = []
for one_new in new:
    if one_new in old:
        for new_value in new.values():
            new_list.append(new_value)
        print(new_list)

for one_old in old:
    if one_old in new:
        for old_value in old.values():
            old_list.append(old_value)
        print(old_list)
        
def inrement():
    increase = new_list[0] - old_list[0]
    increase = new_list[1] - old_list[1]
'''

