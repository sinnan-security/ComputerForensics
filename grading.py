import json
import math
f=open('grades.json')
data=json.load(f)
sigmaf=0
sigmafx=0
v=0
for student in data:
	aggregate=0
	whatever=[]	
	for criteria in data[student]:
		if criteria.startswith("Mid"):
			whatever.append(float(data[student][criteria]))
		else:
			aggregate=aggregate+float(data[student][criteria])
	aggregate=aggregate+max(whatever)
	sigmafx=sigmafx+aggregate
	sigmaf=sigmaf+1
print('Average: {avg}'.format(avg=sigmafx/sigmaf))
for student in data:
	aggregate=0
	whatever=[]	
	for criteria in data[student]:
		if criteria.startswith("Mid"):
			whatever.append(float(data[student][criteria]))
		else:
			aggregate=aggregate+float(data[student][criteria])
	aggregate=aggregate+max(whatever)
	v=v+((aggregate-(sigmafx/sigmaf))*(aggregate-(sigmafx/sigmaf)))
print('Standard Deviation: {std}'.format(std=math.sqrt((v/sigmaf))))
grades=['0.0','1.3','1.7','2.0','2.3','2.6','3.0','3.3','3.6','4.0']
boundries=[]
for i in range(-5,5):
	lower=float(math.floor((sigmafx/sigmaf)+((i+0)/3)*(math.sqrt(v/sigmaf))))
	upper=math.floor((sigmafx/sigmaf)+((i+1)/3)*(math.sqrt(v/sigmaf)))-0.01
	boundries.append([grades[5+i],lower,upper])
	print('Boundries for {grade}: {lower} -> {upper}'.format(grade=grades[5+i],lower=lower,upper=upper))
boundries[0][1]=0
boundries[len(boundries)-1][2]=100
for student in data:
	aggregate=0
	whatever=[]	
	for criteria in data[student]:
		if criteria.startswith("Mid"):
			whatever.append(float(data[student][criteria]))
		else:
			aggregate=aggregate+float(data[student][criteria])
	aggregate=aggregate+max(whatever)
	for i in boundries:
		if(aggregate >= i[1] and aggregate < i[2] ):
			print('ID: {student} TOTAL: {marks} Grade: {grade}'.format(student=student,marks=aggregate,grade=i[0]))
