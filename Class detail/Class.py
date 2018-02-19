#####class method/statistic method
class Employee:
    num_of_emps=0
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

        Employee.num_of_emps+=1

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod  #no default argument needed
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp_1=Employee('Joy','Zhao',50000)
emp_2='Joy-Zhao-50000'

a=Employee.from_string(emp_2)
print(a.first)

print(Employee.raise_amt)

Employee.set_raise_amt(1.05)
print(Employee.raise_amt)

import datetime
my_date=datetime.date(2017,7,8)
print(Employee.is_workday(my_date))

#Special method in class
#double underscore methods

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
#most popular __repr__ goal is to be unambiguous
             #__str__ goal is to be readable
    #将某一类型的变量或者常量转换为字符串对象
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(repr(emp_1))
print(str(emp_1))

#str() 的输出追求可读性，输出格式要便于理解，适合用于输出内容到用户终端。
#repr() 的输出追求明确性，除了对象内容，还需要展示出对象的数据类型信息，
# 适合开发和调试阶段使用

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        first,last=name.split('')
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first=None
        self.last=None


emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.first)
