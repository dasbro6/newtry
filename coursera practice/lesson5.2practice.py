class Person(object):
    Counter = 0

    def __init__(self, name, gender, age, fight_value):
        Person.Counter += 1
        self.name = name
        self.gender = gender
        self.age = age
        self.fig = fight_value

    def battle(self):
        self.fig -= 100

    def practise(self):
        self.fig += 200

    def eat(self):
        self.fig += 80

    def info(self):
        print("I am player {} {}, I have {} fighting value.".format(Person.Counter, self.name, self.fig))


player1 = Person('xiaohua', 'F', 18, 2000)
player1.info()
player1.battle()
player1.eat()
player1.info()
player2 = Person('xiaoqiang', 'M', 19, 1500)
player2.practise()
player2.battle()
player2.eat()
player2.eat()
player2.info()