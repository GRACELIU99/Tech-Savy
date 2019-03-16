##BOOLEAN

print(3>2)
print(3<2)

print(3>2 and 3>5)
#"and" connect both together

print(3>2 or 3<5)
#if one is true, then it is true

print(3>2 or 3>5 or False or 100<100)

n=int(input())
print(n>3)

age=int(input('How old are you?'))
is_in_US=True
answer = input('Are you in US?')
if answer =='no':
    is_in_US=False

if age >= 21:  #boolean
    print('yes, you can,')
else:
    print('sorry, you cannot.')

name= 'aob'
print(name=='aob')
print(name=='oab')
