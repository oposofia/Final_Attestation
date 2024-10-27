from Animals import Animals
from abc import ABC
class PackAnimals(Animals, ABC):
   pass

class Horses(PackAnimals):
    pass

class Donkeys(PackAnimals):
    pass

class Camels(PackAnimals):
    pass