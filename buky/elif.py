# Buky's 7 th video. if, ellif statements

f_name = 'Nafi'
l_name = 'Shahriyar'
space = ' '
name = f_name + space + l_name

print(name)

print("Your age: ")
age = int(input())
if age > 18:
	print("%s Is adult" %name)
elif age < 18:
	print("%s Is not adult" %name)
else:
	print("Something went wrong")

