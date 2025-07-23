class Search:
    def __init__(self):
        pass

    def output_subsets(self):
        input_list = input('请输入一个列表：')

        output_list = []
        for number in input_list[:] :    
            output_list.append([number])
            output_list.append([input_list[:].remove(number)])#这里为什么不能这么用？

        output_list.append(input_list[:])
        output_list.append([])
        print(output_list)

output = Search()
output.output_subsets()






