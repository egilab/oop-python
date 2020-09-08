#self ini mirip kyk this di php

class Humman:
	def __init__(self, umurs, warna=[]): #kyk construct
		self.umur = umurs
		self.warna  = warna

	def get_name(self):
		return 'egi'

	def join_name(self):
		return self.get_name() + ' gusniawan'

	def get_umur(self):
		return 'Umur : ' + str(self.umur)

	def get_warna(self):
		return self.warna


humman = Humman(20, ['merah','biru'])
print(humman.get_name())
print(humman.join_name())
print(humman.get_umur())
print(humman.get_warna()[0])
print(isinstance(humman, Humman)) #cek instance class