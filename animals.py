# Base class for all animals
class Animal:
    def __init__(self, name: str, flight: bool):
        self.name = name
        self.flight = flight  # Indicates if the animal has the ability to fly

    def __str__(self):
        return f"{self.name}, Flight Ability: {'Yes' if self.flight else 'No'}"


# Child class for Birds
class Bird(Animal):
    def __init__(self, name: str, flight: bool = True):  # Default flight is True for birds
        super().__init__(name, flight)


# Test instances for flying/nonflying birds
eagle = Bird(name="Eagle", flight=True)
print(eagle)

penguin = Bird(name="Penguin", flight=False)
print(penguin)