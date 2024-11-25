class Animal:
    '''This is the start of the animal class for 3120.'''

    def __init__(self, animal, species): 
        '''I removed kingdom as a parameter since every animal is in the Animalia kingdom'''
        self.animal = animal
        self.kingdom = 'animalia'
        self.species = species

    def describe(self):
        '''This will print a descriptive sentence about the animal.'''
        return f"{self.animal} is a species of {self.species} in the kingdom {self.kingdom}."

# Testing the describe method
elephant = Animal("The "+"Elephant", "Loxodonta africana")
print(elephant.describe())

class Reptile(Animal):
    '''This is the child class of Animal, which represents reptiles.'''


    def __init__(self, animal, species, venomous=False):
        # Call the parent class's __init__ method to initialize animal and species
        super().__init__(animal, species)
        self.venomous = venomous


    def describe(self):
        '''This method describes whether the reptile is venomous.'''
        is_venomous = "venomous" if self.venomous else "non-venomous"
        return f"{self.animal} ({self.species}) is a {is_venomous} reptile."




# Testing the Reptile class
rattlesnake = Reptile(animal="Eastern Diamondback Rattlesnake", species="Crotalus adamanteus", venomous=True)
anaconda = Reptile(animal="Green Anaconda", species="Eunectes murinus", venomous=False)


# Access attributes and methods
print(rattlesnake.animal, rattlesnake.species, rattlesnake.kingdom)
print(rattlesnake.describe())


print(anaconda.animal, anaconda.species, anaconda.kingdom)
print(anaconda.describe())


