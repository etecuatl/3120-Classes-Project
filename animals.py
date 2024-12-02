# Base class for all animals
class Animal:
    def __init__(self, name: str, flight: bool = False, species: str = None):
        self.name = name
        self.flight = flight  # Indicates if the animal has the ability to fly
        self.species = species

    def __str__(self):
        return f"{self.name}, Flight Ability: {'Yes' if self.flight else 'No'}"

    def describe(self):
        '''Default describe method for Animal.'''
        return f"{self.name} belongs to species {self.species if self.species else 'Unknown'}."


# Child class for Birds
class Bird(Animal):
    def __init__(self, name: str, flight: bool = True):  # Default flight is True for birds
        super().__init__(name, flight)


# Test instances for flying/nonflying birds
eagle = Bird(name="Eagle", flight=True)
print(eagle)

penguin = Bird(name="Penguin", flight=False)
print(penguin)


# Child class for Reptiles
class Reptile(Animal):
    '''This is the child class of Animal, which represents reptiles.'''

    def __init__(self, name: str, species: str, venomous: bool = False):
        # Call the parent class's __init__ method to initialize name and species
        super().__init__(name, flight=False, species=species)
        self.venomous = venomous

    def describe(self):
        '''This method describes whether the reptile is venomous.'''
        is_venomous = "venomous" if self.venomous else "non-venomous"
        return f"{self.name} ({self.species}) is a {is_venomous} reptile."


# Testing the Reptile class
rattlesnake = Reptile(name="Eastern Diamondback Rattlesnake", species="Crotalus adamanteus", venomous=True)
anaconda = Reptile(name="Green Anaconda", species="Eunectes murinus", venomous=False)


# Access attributes and methods
print(rattlesnake.name, rattlesnake.species, rattlesnake.kingdom)
print(rattlesnake.describe())

print(anaconda.name, anaconda.species, anaconda.kingdom)
print(anaconda.describe())

# Testing the describe method
elephant = Animal("The "+"Elephant", "Loxodonta africana")
print(elephant.describe())

