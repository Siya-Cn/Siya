class Employee:
    def __init__(self,first_name,last_name,anual_salary):
        self.first = first_name.title()
        self.last = last_name.title()
        self.salary = anual_salary 

    
    def give_raise(self,total_raise:float=5000):
        self.salary += total_raise
        



    
        