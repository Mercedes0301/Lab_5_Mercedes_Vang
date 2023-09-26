print("Multiplicaion Table")
for i in range(1, 9):
	for j in range(1, 11):
		print(i * j, end='\t') 
	print('')
	
	
print("Prime Number Less Than 250 are: ")
for n in range(2,250):
	for x in range(2, n):
		if n % x == 0:
			break
	
	else:
		print(n)
		
print("All Number Less Then 250") #with prime and unit digit is a 3
def is_prime(n):
	if n <= 1:
		return False
	elif n <= 3:
		return True
	elif n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True
for num in range(2,250):
	if is_prime(num) and num % 10 == 3:
		print(num)
