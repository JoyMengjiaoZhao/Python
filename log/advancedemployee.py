import logging

logger=logging.getLogger(__name__)


file_handler=logging.FileHandler('employee.log')
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)

#logging.basicConfig(filename='employee.log',level=logging.INFO,
#                    format='%(asctime)s:%(levelname)s:%(message)s')
class Employee:
    """A sample Employee class"""

    def __init__(self,first,last):
        self.first=first
        self.last=last

        logger.info('Created Employee: {} - {}'.format(self.email,self.fullname))
    #@property
    def email(self):
        a= '{}.{}@email.com'.format(self.first,self.last)
        return a
  #  @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1=Employee('Chen','Mu')
emp_2=Employee('Hong','Xiao')
emp_3=Employee('La','Xiao')
