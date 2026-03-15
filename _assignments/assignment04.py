# 1) Write a normal function that accepts another function as an argument. 
# Output the result of that other function in your “normal” function.
def get_power(b):
    return b**2

base = 10
exponent = 2
nums = [1, 2, 3, 4, 5]

def my_func():
    print(list(map(get_power, nums)))

my_func()

# 2) Call your “normal” function by passing a lambda function 
# – which performs any operation of your choice – as an argument.
my_num = 2
def my_func1():
    print(list(map(lambda b: b**2, [my_num])))

my_func1()


# 3) Tweak your normal function by allowing an infinite amount of arguments on 
# which your lambda function will be executed. 
my_num = 2
def my_func2(*args):
    return list(map(lambda b: b**2, args))

print(my_func2(1,2,3,4,5,6))

# 4) Format the output of your “normal” function such that numbers look nice 
# and are centered in a 20 character column.
for n in my_func2(1,2,3,4,5,6):
    print('{:^20}'.format(n))