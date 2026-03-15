from oop_assignment.food import Food

class Fruit(Food):
    def __init__(self, name, kind):
        super().__init__(name, kind)

    def clean(self):
        print('I should be cleaned')
