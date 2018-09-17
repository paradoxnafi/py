def isprime(n):

	flag = 0
	for x in range(2, n):
		if n%x is 0:
			flag = 1
			print("%d is not prime" %n)
			break

	if flag is 0:
		print("%d is a prime number" %n)

#n = int(input())
isprime(20580341)