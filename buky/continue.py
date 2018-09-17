# Buky's 11th video, loop

numbers_taken = [2, 4, 1, 5, 4, 6, 18, 12, 15]

print("Available numbers are:")
for item in range(1, 21):
	if item in numbers_taken:
		continue
	else:
		print(item)
