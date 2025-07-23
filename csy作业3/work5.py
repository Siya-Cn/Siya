total = [
    {'sku':'SKU-A','quantity':100},
    {'sku':'SKU-B','quantity':200},
    {'sku':'SKU-C','quantity':400},
    {'sku':'SKU-D','quantity':300}
]


#统计物件总数量我不会
sum = 0
for one_total in total:
    print(one_total)
    sum = sum + one_total['quantity']
print(f"sum = {sum}")
   # number = int(one_quantity.values())
   # sum_quantity = sum(number['quantity'])
   # print(sum_quantity)

#有没有简便方法 只想到了复杂方法 //有
value = "SKU-A"
for one_total in total:
    if one_total['sku'] == value:
        one_total['quantity'] = one_total['quantity'] + 100
print(total)


#怎么把这个新增元素加到列表的最后一位？用-1加在了倒数第二位// 列表的操作
#total.insert(-1,{'sku':'SKU-E','quantity':300})
total.append({'sku':'SKU-E','quantity':300})
print(total)

#能否根据sku的值为SKU-B来进行删除？
for one_total in total:
    if one_total['sku'] == 'SKU-B':
        dict_del = one_total
total.remove(dict_del)
print(total)


new_total = total[-1:]
print(new_total)