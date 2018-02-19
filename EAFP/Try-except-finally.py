
#Try/except block for error edittings

#try:
try:
    f = open('poem.txt')
    if f.name=='poem.txt':
        raise Exception
   # var=bad_var
except FileNotFoundError: #specific
    print('Sorry. The file does not exit')
except Exception as e: #general
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    #pass
    print('Excuting finally...')
