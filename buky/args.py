# Buky's 19th video, taking unknown numbers of input with *args

def add(*args):
	total = 0
	for a in args:
		total += a
	print(total)

add(2, 34, 345, 23546,154 ,34534 ,345 ,3453,4534,2345 ,2345 ,44,1254,45)