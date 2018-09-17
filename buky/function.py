# Buky's 12th video, funcation

def prime(number):
	flag = 0
	for i in range(2, number):
		if number%i is 0:
			print(number, "is not a prime number")
			flag = 1
			break
	if flag is 0:
		print(number, "is a prime number")

print("Enter a number: ")
number = int(input())
prime(number)