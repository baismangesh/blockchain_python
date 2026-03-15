def unlimited_arguments(*args, **keyword_args):
    print(args) 
    for argument in args:
        print(argument)

    print(keyword_args)
    for karg in keyword_args:
        print(karg)
    for karg, varg in keyword_args.items():
        print(karg, varg)

#unlimited_arguments(*[1,2,3,4])
unlimited_arguments(1,2,3,4, name='Mangesh', age=29)

# a = [1,2,3]
# output = 'Some text : {} {} {} '.format(*a)
# print(output)