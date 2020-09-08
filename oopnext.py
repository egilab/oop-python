class Student:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade

	def get_grade(self):
		return self.grade


class Course:
	def __init__(self, max_students):
		self.max_students = max_students
		self.students = []

	def add_student(self, studentx):
		if len(self.students) < self.max_students:
			self.students.append(studentx)
			return 'add success'
		return 'cant add student again'



s1 = Student("Jhon", "18", 80)
s2 = Student("Mike", "18", 70)
s3 = Student("Tom", "18", 60)

course = Course(3)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))

liststudent = course.students
for item in liststudent:
	print(f'{item.name} {item.grade}')