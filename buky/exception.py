#28th video, exception

while True:
	try:
		number = int(input("Enter a number: "))
		print(1024/number)
		break
	except ValueError:
		print("You must entr a number")
	except ZeroDivisionError:
		print("You must not entr 0")
	except:
		break