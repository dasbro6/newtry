class Animal(object):
    def __init__(self, name):
       self.name = name
    def getInfo(self):
       print("This animal's name:", self.name)
    def sound(self):
       print("The sound of this animal goes?")

class Dog(Animal):
    def __init__(self, name, size):
        self.name = name
        self.__size = size

    def getInfo(self):
        print("This dog's name:",self.name)
        print("This dog’s size:",self.__size)


dog = Dog('mimi','small')
dog.getInfo()
dog.sound()