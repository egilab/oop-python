class Person:
	number_person = 0

	def __init__(self, name):
		self.name = name
		Person.add_person()

	@classmethod
	def count_person(cls):
		return cls.number_person

	@classmethod
	def add_person(cls):
		cls.number_person += 5

	@staticmethod #tidak merubah apapun di dalam class
	def add_person20(val):
		return val + 10

p1 = Person("Egi")
p2 = Person("Jhon")
p3 = Person("Tim")
# print(Person.number_person)
# print(p1.name)
# Person.number_person = 4
# print(p1.number_person)
# Person.number_person = 2
# print(Person.number_person)
# print(Person.number_person)
print(Person.add_person20(1))
print(Person.count_person())
