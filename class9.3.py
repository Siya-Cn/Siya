class User :
    def __init__(self,first_name,last_name,sex,age):
        self.first = first_name
        self.last = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = 0

    def describe_user (self):
        print(f'My name is {self.first.title()} {self.last.title()}.')
        print(f'I am a {self.sex} and {self.age} years old.')

    def greet_user (self):
        print(f'Hello {self.first.title()} {self.last.title()}!')
        print('Welcome to log in!')

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts
    

#练习9.7,9.8


class Privileges :
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self) :
        for one_privilege in self.privileges :
            print(f'{one_privilege}')

class Admin(User):
    def __init__(self, first_name, last_name, sex, age):
        super().__init__(first_name, last_name, sex, age)
        self.privileges = Privileges()

administrator = Privileges()
administrator.show_privileges()

example = Admin('jack','doson','male',25) 
example.privileges.show_privileges()


'''
“9.3练习”
user1 = User('julie','xu','female',30)
user1.describe_user()
user1.greet_user()

user2 = User('jack','doson','male',25)
user2.describe_user()
user2.greet_user()

“9.5练习”
user3 = User('rose','doson','female',24)
user3.describe_user()
user3.greet_user()
print(f'You have logged in for {user3.login_attempts} times(time).')
user3.increment_login_attempts()
print(f'You have logged in for {user3.login_attempts} times(time).')
user3.reset_login_attempts()
print(f'You have logged in for {user3.login_attempts} times(time).')
'''