import csv

#with open('names.csv','r') as csv_file:
#    csv_reader=csv.reader(csv_file)    #default is comma
#
#   with open ('new_name.csv','w') as new_file:
#        csv_writer=csv.writer(new_file, delimiter='-')#replace',' with '-'
#        for line in csv_reader:
#           csv_writer.writerow(line)

#dic reader and writer
#with open('names.csv','r') as csv_file:
#    csv_reader=csv.DictReader(csv_file)
#  #  for line in csv_reader:
#  #      print(line)
#    for line in csv_reader:
#        print(line['email'])
with open('names.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)#default is comma
    with open ('new_name.csv','w') as new_file:
        fieldnames=['first_name','last_name']

        csv_writer=csv.DictWriter(new_file, fieldnames=fieldnames,delimiter='\t')#replace',' with '-'
        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
