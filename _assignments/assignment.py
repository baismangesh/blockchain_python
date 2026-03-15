#1 Create two variables – one with your name and one with your age
name = input('Your name please: ')
age = input('Your age please: ')

#2 Create a function which prints your data as one string
def printData():
    print('Hello ' + name + '\nYour age is ' + age)

printData()
#3 Create a function which prints ANY data (two arguments) as one string
def printData(n, a):
     print('Hello ' + n + '\nYour age is ' + a)

printData(name, age)

#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def getAgeInDecade(age):
     return int(age)//10

print("You have lived", getAgeInDecade(age), "decades")