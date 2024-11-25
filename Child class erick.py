from Animal import Animal

class Characteristics(Animal):
    def __init__(self,animal,species):
        Animal.__init__(self,animal,species)
        pass 

    def Mammal(animal):
        while True:
            birth_type = input(f"Does a {animal} give a live birth? Enter 'Yes' or 'No': ")
            if birth_type == "Yes" or birth_type =="yes":
                print("{animal} is a mammal." )
                break
            elif birth_type == "No" or birth_type =="no":
                print("{animal} is not a mammal.")
                break
            else:
                print("Not a valid input.  Please enter a Yes or No")
        return animal
    
