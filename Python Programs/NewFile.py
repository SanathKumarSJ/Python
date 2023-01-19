import csv
'''fields = [ 'Name','Designation','Salary']

row=[['Sanath','CEO',50000],['Yajnesh','Manager',25000],['Roshan','Data Analyst',20000]]

filename="Data.csv"

with open(filename,'w') as csvfile:
	csvwriter= csv.writer(csvfile)

	csvwriter.writerow (fields)

	csvwriter.writerows (row)'''

filename="Data.csv"
fields=[]
rows=[]

with open(filename,'r') as csvfile:
	csvreader = csv.reader(csvfile)

	fields=next(csvreader)

	for row in csvreader:
		rows.append(row)
print('Field names are:'+','.join(field for field in fields))
print('\n First five rows are:\n')
for row in rows[:8]:
	for col in row:
		print("%10s"%col,end=" "),
	print("\n")