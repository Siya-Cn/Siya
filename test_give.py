from employee import Employee

def test_give_default_raise():
    one = Employee('jack','swift',50000)
    one.give_raise()
    assert one.salary == 55000

def test_give_custom_raise():
    one = Employee('jack','swift',50000)
    one.give_raise(10000)
    assert one.salary == 60000


