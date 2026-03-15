import random
import datetime as dt

# 1) Import the random function and generate both a random number between 0 and 1 
# as well as a random number between 1 and 10.
num0to1 = random.random()
print(num0to1)

#num1to10 = random.randrange(1, 10)
num1to10 = random.randint(1, 10)
print(num1to10)

# 2) Use the datetime library together with the random number to generate a random, 
# unique value.
#now = dt.datetime.now().timestamp()
now = dt.datetime.now()
#unique_value = now/num1to10
unique_value = str(num0to1) + str(now)
print(unique_value)
