'''
Base template for animals

what it is?

what it does?

Do you have any pre assumptions?

class name --> start with capital letter

method names --> starts with small letter ... camelCase
'''

class Animal:

    is_animal = True

    def __init__(self, name = '', height = 0, is_predator = False):
        self.__name = name # the __ before the variable to make it a priavt variable that is not accessable by the user but accessable by all the class methods 
        self.height = height
        self.is_predator = is_predator
        self. sound_type = None

    @property              # getter to self.__name variable. as an option to the user to access the privat variables
    def name (self):
        return self.__name

    @name.setter           # setter to self.__name variable. as an option to the user to change the privat variables
    def name(self, new_name):
        self.__name = new_name

    def sound(self, sound_type, db):
        self.sound_type = sound_type
        if db > 10:
            print(f"I am loud, don't \"play\" me on sunday")
        else:
            print(f"I {sound_type}")

    def introduce_yourself(self):
        print(f"I am {self.__name}. My height is {self.height}. Am I a predator? {self.is_predator}")
        print(f"I make {self.sound_type} sound")
        print(f"is animal? {Animal.is_animal}")

    def __repr__(self):
        return f'class variables:'

    def __str__(self):
        return f'I am a {self.__name} and I {self.sound_type}'


dog = Animal('dog', 2, True)
print(dog)
dog.sound('park', 5)
print(dog.sound_type)
dog.introduce_yourself()

cat = Animal()  # to creat an empty instance fromthe class you have tto give a default values to the arguments in the __init__ function

dog.Animal.__name = 'new dog'