import csv

html_output=''
names=[]

with open('patrons.csv','r') as data_file:
    csv_data=csv.DictReader(data_file)

#list/Dic
#    next(csv_data)#We dont want headers or first line of bad data
    next(csv_data)
    for line in csv_data:
        if line['FirstName']=='No Reward':
        #if line[0]=='No Reward':
            break
        names.append("{} {}".format(line['FirstName'],line['LastName']))
        #names.append("{[0]} {[1]}".format(line,line))

html_output += '<p>There are currently {} public contributors. Thank you!</p>'.format(len(names))

html_output+='\n<ul>'

for name in names:
    html_output+='\n\t<li>{}</li>'.format(name)

html_output+='\n</ul>'


print(html_output)



