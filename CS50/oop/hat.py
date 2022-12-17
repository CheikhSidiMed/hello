import random


class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Stytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")