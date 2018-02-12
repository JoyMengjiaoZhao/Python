import pickle
import sys
import os
import numpy as np
class peopleinfo:
    def __init__(self,firstname,lastname,age,gender,telenumber):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.gender=gender
        self.telenumber=telenumber
    def info(self):
        print(self.firstname,self.lastname,':','{}.{}@gmail.com'.format(self.firstname,self.lastname),'telenumber:',self.telenumber,'gender:',self.gender,'age:',self.age)
    def print(self):
        print('Other colleages are:',self.firstname,self.lastname)

def search(contact):
    name = input("The person's firstname you want to find is:")
    for index,member in enumerate(contact,start=1):
        if name == member[0]:
            peopleinfo(member[0],member[1],member[2],member[3],member[4]).info()
            break
        elif index==(len(contact)):
            print('No record!')
def add(membersfile):
        name=input("Please input contactor's firstname, lastname, age, gender, telenumber, for example: Abby,Zhang,18,female,1234")
        list=name.split(',')
        name1=unpickling(membersfile)

        name1=np.vstack((name1,list))

        pickling(name1)
        print(unpickling(membersfile))
def delete(contact):
        firstname=input('The deleting first name is:')
        for index,member in enumerate(contact):
            if firstname==member[0]:
                contact=np.delete(contact,index,axis=0)
        pickling(contact)
def update(contact):
    number=input('The eidtting number is:')
    newnumber=input('Change it to:')
    for member in contact:
        if number==member[4]:
            member[4]=newnumber
    pickling(contact)

def pickling(contact):
    f=open(membersfile,'wb')
    pickle.dump(contact,f)
    f.close()
    del contact

def unpickling(membersfile):
    f=open(membersfile,'rb')
    membersfile=pickle.load(f)
    return membersfile

f=['Abby','Zhang','18','female','1234']
r1=['Babe','Zhao','22','female','2345']
r2=['Chen','Fei','27','male','5678']
c=['Xiang','Chen','22','male','7890']
p1=['Gary','Li','33','male','3456']
p2=['Candy','Liu','35','female','3467']
members=np.vstack((f,r1,r2,c,p1,p2))
membersfile='members.data'
pickling(members)


while True:
    menu = input('''
             1. search
             2. add
             3. delete
             4. view
             5. update
             x. exit
                 ''')
    if menu == '1':
        contact=unpickling(membersfile)
        search(contact)
    elif menu == '2':
        add(membersfile)
    elif menu == '3':
        contact=unpickling(membersfile)
        delete(contact)
    elif menu == '4':
        contact=unpickling(membersfile)
        for member in contact:
            peopleinfo(member[0],member[1],member[2],member[3],member[4]).info()
    elif menu == '5':
        contact=unpickling(membersfile)
        update(contact)
    elif menu == 'x':
        sys.exit()
    else:
      print('Don\'t have this option, please try again!')




