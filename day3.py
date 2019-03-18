def square_plus_one (a):
    result= a*a+1
    return result
print(square_plus_one(2))

print(square_plus_one(10))
# import complex math module
import cmath

a = 1
b = 5
c = 6


# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)


print('The solution are {0} and {1}'.format(sol1,sol2))

def square_plus_one(a, b):
    return a*b+1

print(square_plus_one(2,3))
print(square_plus_one(10,10+10))
def quadratic(a, b, c):
    import math
    x_1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    x_2 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    return x_1,x_2

quadratic(1,-2,1)

#BMI Formula
def calculate_BMI(weight, hight):
    BMI= 703*weight/(height**2)
    if BMI <= 18.5:
        webbrowser.open('https://www.mcdonalds.com/us/en-us.html')
        return "your BMI is {:.1f}. you are underweight.".format(BMI)
    elif 18.5 < BMI <= 25:
        return "your BMI is {:.1f}. You are normal weight.".format(BMI)
    elif 25 <BMI <29.9:
        return "your BMI is {:.1f}. You are over weight.".format(BMI)
    elif BMI>30:
        return "your BMI is {:.1f}. You are obese.".format(BMI)
weight= input ('enter your weight')
height = input ('enter your height')
weight= float(weight)
height=float(height)

print (calculate_BMI(weight, height))



def countdown(n):
    import time
    time.sleep(1)

    if n<=0:
        print('Blassoff!')
    else:
        print(n)
        countdown(n-1)
countdown(5)


name = "Maddison"



name = Grace
for letter in name:
    print(ord(letter))

team = "New England Patriots"

print(len(team))
letter = team [1]
print(letter)

print(team[0])
#print(team[1.0])
print(team[len(team)])


prefixes = 'JKLMOPQ'

suffix = 'ack'
for letter in prefixes:
    print(letter+suffix)

