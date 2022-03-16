class Engine:
	cc=125
	def __init__(self):
		self.mileage=50
		
	def start(self):
		print("Starting",self.mileage)
		
class Bike:
	def __init__(self):
		self.engine=Engine()
		
	def ride(self):
		self.engine.start()
		print(self.engine.mileage)
		
shine=Bike()
shine.ride()
_________________________________________
is a

class Parent:
	fee=500
	def __init__(self):
		self.school="ABCD"
		
	def admit(self):
		print("admission in ",self.school)
		
	@classmethod
	def grow(cls):
		print("Growing every child equallu")
		
	@staticmethod
	def cook():
		print("Cooking")
		
class Child(Parent):
	pass
	
c=Child()
c.cook()
c.admit()
c.grow()
print(c.fee)


_____________________________________________________
class Parent:
	fee=500
	def __init__(self):
		self.school="ABCD"
		
	def admit(self):
		print("admission in ",self.school)
		
	@classmethod
	def grow(cls):
		print("Growing every child equallu")
		
	@staticmethod
	def cook():
		print("Cooking")
		
class Child(Parent):
	def __init__(self):
		self.school="PQRS"
		super().__init__()
		
	def display(self):
		super().cook()
	
c=Child()

c.admit()
c.grow()
print(c.fee)


class GrandChild(Child):
	pass
	
gc=GrandChild()
gc.cook()
gc.admit()
gc.grow()
print(gc.fee)
print(gc.school)


____________________________________________



class Parent:
	def __init__(self,name):
		self.name=name
		
	def choose_career(self):
		print(self.name,"Army")
		
		
class Child(Parent):
	def __init__(self,name):
		self.name=name
		
	def choose_career(self):
		super().choose_career()
		print(self.name,"IT")
		
c=Child("Vengat")

c.choose_career()

	