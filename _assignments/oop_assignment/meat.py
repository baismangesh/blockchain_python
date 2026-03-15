from oop_assignment.food import Food

class Meat(Food):
    def __init__(self, name, kind):
        super().__init__(name, kind)

    def cook(self):
        print('I should be cooked')

