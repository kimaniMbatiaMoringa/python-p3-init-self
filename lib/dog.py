#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = "Mutt"):         #Runs whenever a instance of the class is created
        self.name = name
        self.breed = breed
        #print(f"{name} is born!")
    pass



    #def bark(self):
    #    print("Woof!")

    #def adopt(self,owner_name):
    #    self.owner = owner_name    

#fido = Dog("Fido")        