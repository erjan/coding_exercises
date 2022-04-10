'''

Implement a Class named Dog and a Class named Animal follow the rules below:

Class Dog inherited from Class Animal.
Implement a classmethod named show_species in Animal to print the species of the class that call this method, like this It's dog!
Implement a barking method in Class Dog, print something like Brown Pug is barking!. Brown is the color of the dog and Pug is the breed of the dog. Checkout how the two attributes been initialized in the constructor method of Dog.
Implement access and modify of the private attributes __color in Dog. You need to implement it by property and setter so that we could get a dog's color by access dog.color and change it by doing dog.color = 'Black'.

'''

class Animal:
    species = 'animal'

    # write a class method show_species to print the species of the class
    # like this "It's dog". so that every subclass could call the same method
    # to print their own species
    # -- write your code here --
    @classmethod
    def show_species(cls):
        print("It's " + cls.species + '!')


# Make Class Dog inherit from Class Animal
# -- write your code here --
class Dog(Animal):
    species = 'dog'

    def __init__(self, breed):
        self.__breed = breed
        self.__color = 'undefined'

    def barking(self):
        # print something like `Black Alaskan is barking!`
        # -- write your code here --
        print('%s %s is barking!' % (self.__color, self.__breed))

    # write a property function to return the color of the Dog that stores
    # at self.__color
    # -- write your code here --
    @property
    def color(self):
        return self.__color
    

    # write a setter function to change the dog's color which stores at
    # self.__color
    # -- write your code here --
    @color.setter
    def color(self, color):
        self.__color= color
