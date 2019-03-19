AFC_East = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
a= [42, 123]
c= []
#print len(AFC_East))
AFC_East_Best = ['New England Patriots']

#print(len(AFC_East_Best))

str_team = 'New England Patriots'
#print(len(str_team))

#print(str_team[0])
print(AFC_East[1])
print('Miami Dolphins' in AFC_East)

for whatever in AFC_East:
    print(whatever)

print(AFC_East)
AFC_East[-1] = 'New York Giants'
print(AFC_East)

#Dictionary

names= ['Bailey', 'Aob', ' Maddison']
scores= [60, 90, 100]
#grades = dict()

grades = {}
grades['Bailey'] = 60

grades ['Maddison']= 100

print(grades)
print(grades ['Maddison'])

print ('Penny' in grades)
print(len(grades))
print()

for names in grades.keys():
    print(names)
for score in grades.values():
    print(score)
for item in grades.items():
    print(item)
