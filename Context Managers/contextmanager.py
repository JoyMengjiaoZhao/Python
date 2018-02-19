from contextlib import contextmanager

#write text to the file
@contextmanager
def open_file(file,mode):
    try:
        f=open(file,mode)
        yield f
    finally:
        f.close()

with open_file('sample.txt','w') as f:
    f.write('I will always love u')

print(f.closed)

#change direction and print the list of direction
import os
@contextmanager
def change_dir(destination):
    try:
        cwd=os.getcwd()  #get the current workin dictionary (cwd)
        os.chdir(destination) #change it to the destination
        yield
    finally:
        os.chdir(cwd)   #return back to the cwd

with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())
