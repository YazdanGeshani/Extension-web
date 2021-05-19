"""cette classe permis de definir l'objet(c'est a dire nous allons donner des 
attributs a un objet pour le definir)"""
class Pet:
	def __init__(self, name, greeting = "Hello"):
		self.name = name
		self.greeting = greeting
"""ici on définit l'action dont va faire cet objet"""
	def say_hi(self):
		print(f"{self.greeting}, I'm {self.name}!")
"""ici on fait un objet(chat) grace a la class pet deja créér"""
class Cat(Pet):
	def __init__(self, name):
		super().__init__(name, "Meow")

my_pet = Pet("Gaston")
my_pet.say_hi()