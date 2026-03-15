from vehicle import Vehicle

class Car(Vehicle):
    # top_speed = 100
    # warnings = []

    def brag(self):
        print('look how cool my car is!')

print('-- car1 --')    
car1 = Car()
car1.drive()

#Car.top_speed = 200
car1.add_warning('New warning')
#car1.__warnings.append([])
#print(car1.__dict__)
print(car1)

print('-- car2 --')
car2 = Car(200)
print(car2.get_warnings())
car2.drive()

print('-- car3 --')
car3 = Car(250)
print(car3.get_warnings())
car3.drive()
car3.brag()