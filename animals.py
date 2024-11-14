class Animal:
    '''This is the start of the animal class for 3120.'''

    def __init__(self, animal, species): 
        '''I removed kingdom as a parameter since every animal is in the Animalia kingdom'''
        self.animal = animal
        self.kingdom = 'animalia'
        self.species = species

# Testing to see if the code works
elephant = Animal("Elephant", "Loxodonta africana")
print(elephant.animal)
print(elephant.kingdom)
print(elephant.species)