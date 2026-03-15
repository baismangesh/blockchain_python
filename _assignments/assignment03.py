# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
person1 = {'name': 'abc', 'age': 20, 'hobbies': ['reading','skiing']}
person2 = {'name': 'xyz', 'age': 30, 'hobbies': ['fishing','hiking']}
persons = [person1, person2]

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
names = [el['name'] for el in persons]
print(names)

# 3) Use a list comprehension to check whether all persons are older than 20.
def older_than_20(age):
    return age > 20
print(all([older_than_20(el['age']) for el in persons]))

# 4) Copy the person list such that you can safely edit the name of the first person 
# (without changing the original list).
copied_persons = persons[:]

# 5) Unpack the persons of the original list into different variables 
# and output these variables.
for person in persons:
    name, age, hobbies = person.items()
    print(name, age, hobbies)