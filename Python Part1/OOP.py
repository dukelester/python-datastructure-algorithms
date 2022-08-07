class Car:
    def __init__(self, modelName, color):
        self.modelName = modelName
        self.color = color
        
    
    def display(self):
        print(self.modelName, self.color)

mazda = Car("mazda", "white")

mazda.display()

class Student:    
    count = 0    
    def __init__(self):    
        Student.count = Student.count + 1    
s1=Student()    
s2=Student()    
s3=Student()    
print("The number of students:",Student.count)    


#inheritance
class Animal:
    def __init__(self, color, type_):
        self.color = color
        self.type_ = type_

    def eating(self, food):
        print(f"This anomal eats {food}")


#a child class
class Cow(Animal):
    
    def __init__(self, milk_litres, farmer):
        # super().__init__( color, type_)
        self.milk_litres = milk_litres
        self.farmer = farmer


    def feedCow(self, food_type ):
        print(f"the cow is eating {food_type}")


animal = Animal("White", "cattle")
animal.eating("Grass")

my_cow = Cow(30, "John Kangethe")
my_cow.feedCow("neippier grass")

my_cow.eating("its food")
print(my_cow.color)