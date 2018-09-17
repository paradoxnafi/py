# Buky's 18th video, unpacking args,

def volume(length, height, width):
	area = length*height*width
	print(area)
item1 = [20, 30, 2]
item2 = [3, 4, 5]

volume(item2[0], item2[1], item2[2])
volume(*item1)# Here we are unpacking data froma a list and passing it to a argument
volume(*item2) # Here we are unpacking data froma a list and passing it to a argument