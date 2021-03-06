class Employee:
    """A sample Employee class"""

    def __init__(self,first, last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1=Employee('Chen','Mu',60000)
emp_2=Employee('Hong','Xiao',70000)
