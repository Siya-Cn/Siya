class String:
    def __init__(self):
        self.string = ''  #为什么这里用self.string =【】

    def get_string(self):
        user_input = input('Please input a string:')
        self.string = user_input  #这里调用append函数 self.string.append(user_input)
                                       #跑不出来？
        
    def print_string(self):
        print(self.string.upper())

message = String()
message.get_string()
message.print_string()
