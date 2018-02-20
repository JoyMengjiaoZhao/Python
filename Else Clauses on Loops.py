def find_index(to_search,target):
    for i,value in enumerate(to_search): #need index and value
        if value==target:
            break
    else:    #there is not loop
        return -1
    return i
my_list=['Corey','Joy','Chen']
index_location=find_index(my_list,'Steve')

print('Location of target is index: {}'.format(index_location))
