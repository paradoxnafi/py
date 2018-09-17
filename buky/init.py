# 30th video, init

'''
class Tuna:

	def __init__(self):
		print('BlahBlahBlah')

	def swim(self):
		print('Lets swim')

a_var = Tuna()
a_var.swim()
'''

class Enemy:
	
	def __init__(self, x):
		self.energy = x
	
	def get_energy(self):
		print(self.energy)


nahid_takla = Enemy(5)
seikh_hasina = Enemy(10384513)

nahid_takla.get_energy()
seikh_hasina.get_energy()
		