from random import randint


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitdown!")

    def sleep(self):
        print(self.name.title() + " is sleeping now")

    def talk(self, master):
        if master:
            print("the stranger dog " + self.name.title() + " is talking with itself")
        else:
            print("the stranger dog " + self.name.title() + " is talking with " + master)


class Die:
    def __init__(self):
        self.sides = 6

    def roll_die(self, sides):
        self.sides = sides
        for i in range(0, self.sides):
            print(i)
            print("now the value is " + str(randint(1, self.sides)))
