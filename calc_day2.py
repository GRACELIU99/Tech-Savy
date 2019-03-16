NUMBER_OF_SECONDS_IN_ONE_MINUTE = 60
seconds =42*60+42
print("There are {} seconds ...". format(seconds))


NUMBER_OF_SECONDS_IN_ONE_MINUTE = 60
seconds = 42 * NUMBER_OF_SECONDS_IN_ONE_MINUTE+42
print('There\'s {} seconds ...'. format (seconds))


NUMBER_OF_KILOMETERS_IN_A_MILE = 1.61
MILES = 10/NUMBER_OF_KILOMETERS_IN_A_MILE
print ("There are {} miles in 10 kilometers...". format (MILES))


NUMBER_OF_KILOMETERS_IN_A_MILE = 1.61
MILES = 10/NUMBER_OF_KILOMETERS_IN_A_MILE
print ("There are {:.2f} miles in 10 kilometers...". format (MILES))


NUMBER_OF_KILOMETERS_IN_A_MILE = 1.61
MILES = 10/NUMBER_OF_KILOMETERS_IN_A_MILE
print ("There are {:.3f} miles in 10 kilometers...". format (MILES))


#compute te percentage of te hour that has elapsed.
minute = 45
percentage = (minute*100)/60
print('45 minutes is equal to {}% of one hour...'. format (percentage))

#what is the volume of a sphere with radius 5
import math
r=5
volume = (4/3)*math.pi*math.pow(r,3)
print('The volume of the sphere {} is {:.3f}.'. format(r, volume))


##
print("My name is {:.1}.". format('Grace'))


##
import math
r=input('Please enter a number')
print(type(r))

r=int(r)
print('After conversion,', type(r))

volume = (4/3)*math.pi*math.pow(r,3)
print ('the volume of a sphere of {} is {:.3}. ' . format(r, volume))


#1.3
hour = 13
min = 2
print('Current time is {:2}:{:02}.'. format(hour , min))


##
print(1+2)


##
import datetime
print(datetime.datetime.now())


now = datetime. datetime.now()
print(now)
print(now.hour, now.minute, now.second)
print (now. year)

import math
print(math.pi)
print(math.sqrt(25))

import random
print(random. random())
print(random.random()*100)
print(random.random()*100) # a random integer between 0 and 100

print(random.randint(1, 6)) # a random integer between 1 and 6

print(random.choice(['valerie','Grace', 'Aob'])) # a random name in the list

lower= int(input('Place a number as the lower bound'))
upper= int(input('another one as upper bound'))
print(random.randint(lower,upper))


##springs
#I'm "ok"
print("I'm \" ok\". ")
print('I\'m learning\n\nPython.')
