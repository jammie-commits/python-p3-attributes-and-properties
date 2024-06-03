#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    approved_breeds = ["Pug", "Bulldog", "Beagle", "Labrador", "Golden Retriever"]

    def __init__(self, name="", breed=""):
        self._name = None
        self._breed = None
        self.set_name(name)
        self.set_breed(breed)

    @property
    def name(self):
        return self._name   

    @name.setter 
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in self.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    def set_name(self, name):
        self.name = name

    def set_breed(self, breed):
        self.breed = breed  
