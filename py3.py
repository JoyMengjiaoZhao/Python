
"""命令行火车票查看器（the head）
Usage:
	py3 [-gdtkz] <from> <to> <date>
Options:
    -h,--help   帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -r          高级软卧
    -k          快速
    -z          直达

Example:
    #查询5月10日北京到上海所有车次
    python py3.py 北京 上海 2017-05-10
    #查询5月10日南京到上海的动车和高铁
    python py3.py -dg 南京 上海 2017-05-10

"""

print('a',end=' ')
print('b')

i=5
print('the area is',i)

number=2
#guess=int(input('enter a numner:'))

#if guess==number:
#    print('hahhaha')
#elif guess>number:
 #   print('nononono')
#else:
 #   print('heiheihei')

# while......else.....
#running=True
#while running:

#    guess=int(input('enter an integer： '))
#    if guess == number:
 #       print('Look!')
 #       running=False
 #   elif guess<number:
 #       print('Look at!')
 #   else:
 #       print('Look at it!')

#else:
#    print('Over!')
 #   print('Done')

#for i in range(1,5):
#    print(i)
#else:
#    print('lalala')

#    print(list(range(5)))

#while True:
#    s=input('enter something: ')
#    if s=='quit':
#        break
 #   print('length is',len(s))#length
#print('done!')

import random
import time

#def hello():
#    print('hello')
#hello()

c=50
def print_adder(a,b=2):
    global c #全局变量
    c=a+b
    print('c equals', c)
print_adder(1)
print_adder(1,5)
print_adder(b=3,a=6)

def total(a=5,*numbers,**phonebook):
    print('a',a)
    for single_item in numbers:
        print('single_item', single_item)
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,Jack=1123,Jone=2231,Inge=1560))

def maxx(x,y):
    '''compare and see results'''
    if x>y:
        return x
        '''print(x,'is maximum')'''
    elif x==y:
        '''return 'equal'''''
        print('It is equal')
    else:
        '''return y'''
        print(y,'is maximum')
maxx(3,4)
print(maxx.__doc__)
'''check the doc words'''

import module

for i in module.i:
    print(i)
'''print('The pythonpath is',module.path,'\n')'''


if __name__=='__main__':
    print('Run by itself')
else:
    print('Be imported')

dir(module)
'''dont understand dir'''
'''package'''

shoplist = ['egg','apple','meat']
print('I have',len(shoplist),'items to purchase.')
print('These items are',end=' ')
for item in shoplist:
    print(item,end=' ')
    '''end=' ' means the ending is not \n'''

print('\n I also need to buy rice')
shoplist.append ('rice')
print('My shopping list is now',shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem=shoplist[0]
del shoplist[0]
print('I bought the',olditem)
print('MY shopping list is now',shoplist)

'''Tuple'''
print('\n')
zoo=('monkey','dog','cat')
print('The number in the zoo is',len(zoo))
print('The zoo contains',zoo)
new_zoo='cow','snake',zoo
print('The number of new zoo is',len(new_zoo))
print('The new zoo contains',new_zoo)
print('The old zoo animals are',new_zoo[2])
print('The last animal of old zoo animals is',new_zoo[2][2])

addressbook={
    'a':'apple',
    'b':'boy',
    'c':'candy',
    'd':'dance'
}
print('The description for a is', addressbook['a'])

del addressbook['b']
print('\nThere are {} contacts in the address-book'.format(len(addressbook)))
print('There are',format(len(addressbook)),'contacts in the address-book\n')
for name,address in addressbook.items():
    print('Contact {} at {}'.format(name,address))

addressbook['e']='error'
print('The addressbook is', addressbook)
if'e' in addressbook:
    print('\n e is',addressbook['e'])

fruitlist=['apple','banana','orange']
name='joy'
print('Item 0 is', fruitlist[0])
print('Item -1 is', fruitlist[-1])
print('The first character of name is', name[0])

print('Item 0 to 2 is', fruitlist[0:2])
print('Item start to end is', fruitlist[:])
print('selected fruit is',fruitlist[::2] )


'''Collection???'''
mylist=fruitlist
del fruitlist[0]
print('mylist is ',mylist)
print('fruitlist is',fruitlist)

mylist=fruitlist[:]
del mylist[0]
print('mylist is ',mylist)
print('fruitlist is',fruitlist)

'''beau'''
#name=input('Input a word:')
name='beau'
if name.startswith('bea'):
    print('Yes,it is')
if 'a' in name:
    print('Yes, it has "a"')
if name.find('s')==-1:
    print('No,it does not have "s"')
if name.find('ab'):
    print('Yes, it has "ab"')

delimiter='_*_'
print(delimiter.join(fruitlist))

class Person1:
    def say_hi(self):
        print('I miss u')
Person1().say_hi()

class Person2:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print('Hello,my name is',self.name)
Person2('Swaroop').say_hi()


class Robot:
    #population=0
    def __init__(self,name,population):
        self.name=name
        self.population=0
        print("(Initializing{})".format(self.name))
        self.population+=1
    def die(self):
        print("{} is being destroyed!".format(self.name))
        self.population -= 1
        if self.population==0:
            print("{}was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(self.population))
    def say_hi(self):
        print("Greetings,my masters call me {}.".format(self.name))
    #@classmethod
    #def how_many(cls):
      #  print("We have {:d} robots.".format(cls.population))

droid1=Robot("R2-D2",'0')
droid1.say_hi()
#Robot.how_many()

droid2=Robot("C-3PO",'0')
droid2.say_hi()
#Robot.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()
#Robot.how_many()

class info:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print(self):
        print(self.name,self.age)

student1=info('Jack','18','male')
student1.print()
#Inheritance
class SchoolMember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('(Initialized SchoolMember: {})'.format(self.name))
    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name,self.age),end=" ")

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        #SchoolMember.__init__(self,name,age)
        super().__init__(name,age) #super() lets you avoid referring
        # to the base class explicitly, which can be nice.
        # But the main advantage comes with multiple inheritance,
        # where all sorts of fun stuff can happen.
        self.salary=salary
        print('(Initialized Teacher:{})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{:d}"'.format(self.salary))
class Student(SchoolMember):
    def __init__(self,name,age,marks):
        #SchoolMember.__init__(self,name,age)
        super().__init__(name,age)
        self.marks=marks
        print('(Initialized Student: {})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{:d}"'.format(self.marks))
t=Teacher('Mrs.Shrividya',40,30000)
s=Student('Swaroop',25,75)

print()
members=[t,s]

print(isinstance(t,Teacher))#t belongs to Teacher in instance
print(issubclass(Student,SchoolMember))#Student belongs to SchoolMember in class

def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text==reverse(text)

something='abba'
if is_palindrome(something):
    print("Yes,it is a palindrome")
else:
    print("No, it is not a palindrome")

poem='''\I love Python!'''
f=open('poem.txt','w')
f.write(poem)
f.close()

f=open('poem.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line,end='')
f.close()

print('\n')
f=open('text','r')
print(f.name)
print(f.mode)
f.close()
############Read file###########
#with open('text','r') as f:
    #f_contents1=f.read()
    #print(f_contents1)

    #f_contents2=f.readlines()
    #print(f_contents2)

    #f_contents3=f.readline() #next by next
    #print(f_contents3)

    #for line in f:
     #   print(line,end='')

    #size_to_read=10
    #f_contents=f.read(size_to_read)
    #while len(f_contents)>0:
    #   print(f_contents,end='*')
    #   f_contents=f.read(size_to_read)

    #size_to_read=10
    #f_contents=f.read(size_to_read)
    #print(f_contents)
    #f.seek(3)
    #f_contents=f.read(size_to_read)
    #print(f_contents)

##########Write file#########
#with open('textwrite','w') as f:
#    f.write('Write')

with open('text','r') as rf:
    with open('text_copy','w') as wf:
        for line in rf:
            wf.write(line)
#copy the image
#with open('Photo.jpg','rb') as rf:
#    with open('photo_copy.jpg','wb') as wf:
#        for line in rf:
#            wf.write(line)

with open('Photo.jpg','rb') as rf:
    with open('photo_copy.jpg','wb') as wf:
        chunk_size=4096
        rf_chunk=rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk=rf.read(chunk_size)

import pickle
shoplistfile='shoplist.data'
shoplist=['apple','mango','carrot']

f=open(shoplistfile,'wb')
pickle.dump(shoplist,f)
f.close()  #pickling

del shoplist

f=open(shoplistfile,'rb')
storedlist=pickle.load(f)
print(storedlist) #unpickling

a=('ab,b,c')
b=a.split(',')
print(b)

filename = 'phonebook.data'
f = open('phonebook.data', 'wb')
contactlist = {'elizabeth':'test@163.com,13512345678,Beijing Chaoyang district'}
pickle.dump(contactlist, f)
f.close()
del contactlist
f=open(filename,'rb')
storedlist=pickle.load(f)
print(storedlist)

s = ","
seq = ('a', 'b', 'c'); # This is sequence of strings.
print (s.join( seq ))
a=[a,s.join( seq )]
print(a)

def a( ):
    return 1
b=a()
print(b)

#fizzbuzz
def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

print ("\n".join(fizzbuzz(n) for n in range(1, 101)),'\n')

for x in range(1,101): print("fizz"[x%3*4:]+"buzz"[x%5*4:] or x)
# detailed explaination https://www.quora.com/How-do-I-understand-this-piece-of-Python-code-question-and-code-in-the-details-below
print(3^2)
print("Pete loves Ann"[5:] )

#fibonacci
#recursion
for n in range(1,10):
    def fun(n):
        if n==1 or n==2:
            n=1
        else:
            n=fun(n-1)+fun(n-2)
        return n
    print(fun(n))
#[2]
a, b=0, 1
for i in range(0,10):
     print (a)
     a,b=b,a+b
#[3]Fibonacci Generator
def fib(num):
    a,b=0,1
    for i in range(0,num):
        yield "{}:{}". format(i+1,a)
        a,b=b,a+b
for item in fib(10):
    print(item)
#list,tuples,dictionaries,sets
#list
my_list=[10,20,30,40,50]
for i in my_list:
    print (i)

#Tuples
my_tup=(1,2,3,4,5,6,7,8,10)
for i in my_tup:
    print (i)

#Dict
my_dict={'name':'Bronx','age':'2','occupation':'Corey Dog'}
#for key,val in my_dict.iteritems():
#    print ("my {} is {}".format(key,val))

#set
my_set={10,20,20,30,40,50,10,20,30,40,50}
for i in my_set:
    print (i)

#list methods
a=['matt','joy','babe','chen']

a.append('art')
print(a)

b=['boy','girl']
a.insert(0,b)
print(a)

a.extend(b)
print(a)

a.remove(b)
print(a)

c=a.pop()
print(a)
print(c)

a.reverse()
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

d=sorted(a)
print(a)
print(d)

e = [1,2,3,4]
print(min(e))
print(max(e))
print(sum(e))

print(a.index('matt'))

for index,item in enumerate(a,start=1):
    print(index,item)

a_str='-'.join(a)
print(a_str)

new_a=a_str.split('-')
print(new_a)

#sets
setsa={'a','b','c','d','a'}
print(setsa)

setsb={'a','b','c','d'}
setsc={'a','b','e','f'}
print(setsb.intersection(setsc))
print(setsb.difference(setsc))
print(setsb.union(setsc))

empty_list=[]
empty_list=list()

empty_tuple=()
empty_tuple=tuple()

empty_set=set()

empty_dict=dict() #empty dict
#empty_dict[key]=value #defination

#Dictionary
student={'name':'John','age':25,'courses':['Math','CompSci']}
print(student['name'])
print(student.get('name'))
student.update({'name': 'Abby','age':13,'phone':'234'})
#del student['age'] #中括号
age=student.pop('age')
print(student)
print(age)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
for key in student:
    print(key)
for key,value in student.items():
    print(key,value)

#dictionary in hashtable(find sum pairs for 10)
def pair10(given_list):
    numbers_seen={}
    for item in given_list:
        if (10-item) in numbers_seen:
            print(str(10-item)+','+str(item))
            return
        else:
            numbers_seen[item]=1
    print('There is no pairs for sum 10')
pair10([1,2,6,4,8])

#list comprehension
nums=[1,2,3,4,5,6,7,8,9,10]
my_list=[n for n in nums]
print (my_list)

my_list=[n*n for n in nums]
print (my_list)

my_list=list(map(lambda n: n*n, nums)) #n is input n*n is anonymous function
print(my_list)

g=lambda n:n*n
print(g(2))

# I want 'n' for each 'n' in nums if 'n' is even
my_list=[n for n in nums if n%2==0]
print (my_list)

my_list=list(filter(lambda n:n%2==0,nums))
print (my_list)


my_list=[(letter,num) for letter in 'abcd' for num in range(4)]
print (my_list)

#dictionary comprehension
names=['a','b','c','d']
heros=[1,2,3,4]
print ('\n',list(zip(names,heros)))
my_dict={name:hero for name,hero in zip(names,heros) if name !='a'}
print (my_dict)

#set comprehension
nums=[1,1,2,3,4]
my_set={n for n in nums}
print (my_set)

#generator expressions
# I want to yield 'n*n' for each 'n' in nums
nums=[1,2,3,4,5,6,7]
my_gen=(n*n for n in nums)
for i in my_gen:
    print (i)

#generator&&list comprison
names=['John','Corey','Adam','Steve','Rick']
majors=['math','engineering','arts','business','finance']
#1.list
def people_list(num_people):
    result=[]
    for i in range(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
        }
        result.append(person)
    return result
#2.generator
def people_generator(num_people):
    for i in range(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
        }
        yield person
t1=time.clock()
#people=people_list(1000000)
people=people_generator(1000000)
t2=time.clock()
print('Took {}seconds:'.format(t2-t1))
#which means generator everytime loop once and give the answer, which save the memory.

#formatting
person={'name':'Joy','age':18}
sentence='My name is {} and I am {} years old'.format(person['name'],person['age'])
print(sentence)
sentence='My name is {0} and I am {1} years old'.format(person['name'],person['age'])
print(sentence)
sentence='My name is {0[name]} and I am {1[age]} years old'.format(person,person)
print(sentence)
sentence='My name is {0[name]} and I am {0[age]} years old'.format(person)
print(sentence)
l=['Joy',18]
sentence='My name is {0[0]} and I am {0[1]} years old'.format(l)
print(sentence)
sentence='My name is {name} and I am {age} years old.'.format(name='Joy',age=18)
print(sentence)
for i in range(1,10):
    sentence='The value is {:03}'.format(i)
    print(sentence)
pi=3.1425
sentence='Pi is equal to {:.3f}'.format(pi)
print(sentence)
sentence='1 Mb is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)
import datetime
my_date=datetime.datetime(2016,9,24,12,30,45)
print(my_date)
sentence='{0:%B %d,%Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)
##
a=['|ab|b|c','|ab|b|c']
b=a[0].split('|')
print(b)

a=['a','b']
print(a[-1])

## 按行添加数据
import prettytable as pt
tb = pt.PrettyTable()
tb.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
tb.add_row(["Adelaide",1295, 1158259, 600.5])
tb.add_row(["Brisbane",5905, 1857594, 1146.4])
tb.add_row(["Darwin", 112, 120900, 1714.7])
tb.add_row(["Hobart", 1357, 205556,619.5])
print(tb)

#if __name__ == "__main__": meaning
import module
print("top-level in two.py")
module.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")

names=['John','Corey','Adam','Steve','Rick']
majors=['math','engineering','arts','business','finance']
def people_generator(num_people):
    for i in range(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
        }
        yield person
people=people_generator(2)
print (next(people))

class Person1:
    def say_hi(self):
        print('I miss u')
if __name__ == '__main__':
    Person1()

from module import * #import everthing from module
import sys
print(sys.path) #find path

courses=['a','b','c','d']
random_course=random.choice(courses)
print(random_course)
# common function
import random
import datetime
import calendar
today=datetime.date.today()
print(today)

# rename the file
import os

os.chdir('/Users/joyzhao/Desktop/Allfiles')
print(os.getcwd())
for f in os.listdir():
    print(f)

###Generators

#def square_number(nums):
#    for i in nums:
#        yield(i*i)

#my_nums=square_number([1,2,3,4,5])

my_nums=(x*x for x in [1,2,3,4,5])

print (my_nums)
print (list(my_nums))

for num in my_nums:
    print(num)

##decorators
def outer_functions():
    message='Hi'
    def inner_function():
        print(message)
    return inner_function()
outer_functions()

def outer_function():
    message='Hi'
    def inner_function():
        print(message)
    return inner_function  #a function waitting to be excuated
my_func=outer_function()
my_func()

def outer_function(msg):
    message=msg
    def inner_function():
        print(message)
    return inner_function
hi_func=outer_function('hi')
bye_func=outer_function('bye')
hi_func()
bye_func()

#decorator
def decorator_function(original_function):    #option one for decoration :function
    def wrapper_function(*args,**kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

#class decorator_class(object):   #option two for decoration :class
#    def __init__(self,original_function):
#        self.original_function=original_function
#    def __call__(self,*args,**kwargs):
#        print('call method executed this before {}'.format(self.original_function.__name__))
#        return self.original_function(*args,**kwargs)

@decorator_function  #decorator signal
#@decorator_class
# equal: decorated_display=decorator_function(display)
def display():
    print('display function ran')

#decorated_display=decorator_function(display)
#decorated_display()
@decorator_function
#@decorator_class
def display_info(name,age):
    print('display_info ran with arguments({},{})'.format(name,age))

display_info('John',25)
display()

#####Namedtuple
from collections import namedtuple
color=(55,155,255)  #tuple
print (color[0])
color={'red':55,'green':155,'blue':255}
print(color['red'])

Color=namedtuple('Color',['red','green','blue'])
color=Color(55,155,255)
color=Color(red=55,green=155,blue=255)
print(color.red)
print (color[0])



