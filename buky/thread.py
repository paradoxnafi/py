import threading

class print_name(threading.Thread):
	def run(self):
		for _ in range(10000000000):
			print(threading.currentThread().getName())

x = print_name(name = 'first')
y = print_name(name = 'second')

x.start()
y.start()