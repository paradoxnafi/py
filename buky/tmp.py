flag = 0

print("Enter a number: ")
number = int(input())

for i in range(2, number):
	if number%i is 0:
		print(number, "is not a prime number")
		flag = 1
		break
if flag is 0:
	print(number, "is a prime number")
