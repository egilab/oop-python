#perdalam lagi tentang super()

class Animals:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f'hello my name is {self.name} and Im {self.age} years old')

	def speak(self):
		print("i dont know what your speak")

	def listfood(self):
		return 'sugar, meat, milk, fishx'

class Cat(Animals):
	def __init__(self, name, age, color):
		super().__init__(name , age)
		self.color = color

	def speak(self):
		print(f'Im speak meow and my name is {self.name} my color is {self.color}')

class Dog(Animals):
	def __init__(self, name, age, color):
		super().__init__(name, age)
		self.color = color

	def speak(self):
		print(f'Im speak bark and my name is {self.name} my color is {self.color}')

	def getfood(self):
		return self.listfood()

	def formouse(self):
		print('chesse, soap, tshirt')

class Mouse(Dog, Cat):
	def __init__(self, name, age, color):
		super(Dog, self).__init__(name, age, color)

	def getmousefood(self):
		return self.getfood()

	def getdata(self):
		print(f'my name {self.name} my color is {self.color}')

cat = Cat('kitty', 8, 'red')
cat.speak()

dog = Dog('Doggy', 10, 'blue')
dog.speak()
print(dog.getfood())

print('---')

mouse = Mouse('mousy',2, 'black')
print(mouse.getmousefood())
mouse.getdata()