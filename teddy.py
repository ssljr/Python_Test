import dog


class Teddy(dog.Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def fight(self):
        print("teddy "+self.name+" like fighting!")
