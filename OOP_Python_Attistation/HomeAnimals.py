from Animals import Animals
from abc import ABC
class HomeAnimals(Animals,ABC):
    pass
class Cats(HomeAnimals):
    pass

class Dogs(HomeAnimals):
    pass

class Hamsters(HomeAnimals):
    pass