# 1) Create a list of names and use a for loop to output the length of each name (len()).
# 2) Add an if check inside the loop to only output names longer than 5 characters.
# 3) Add another if check to see whether a name includes a “n” or “N” character.
# 4) Use a while loop to empty the list of names (via pop())

#initializing names list
more_names_to_add = True
names = ['']
# 1) Create a list of names and use a for loop to output the length of each name (len()).
while more_names_to_add:
    name = input('Enter name to be added into the list: ')
    names.append(name)
    choice = input('Do you have more names to added? (Y/N): ')
    if choice != 'Y':
        more_names_to_add = False

print('Name longer than 5 characters')
print('-' * 10)
for name in names:
    #2) Add an if check inside the loop to only output names longer than 5 characters.
    if len(name) > 5:
        print(name)

print('Name contains character n or N')
print('-' * 10)
for name in names:
    # 3) Add another if check to see whether a name includes a “n” or “N” character.
    if 'n' in name or 'N' in name:
        print(name)

# # 4) Use a while loop to empty the list of names (via pop())
print("before emptying")
print('-' * 10)
print(names)
while len(names)>0:
    names.pop()

print("after emptying")
print('-' * 10)
print(names)