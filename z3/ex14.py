from sys import argv

script, user_name = argv
promt = '=> '

print(f"Hello {user_name}! I am {script}")
print("Where do you live")
live = input(promt)

print("Do you like me?")
like = input(promt)

print("What computer do you have?")
computer = input(promt)

print(f'''
So you have said that Your name is {user_name}.
You live in {live}. You have a {computer} computer.
Great
	''')