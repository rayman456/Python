import random

k = input("Enter a number:")
k = int(k)
total = 0
for i in range(0, k):
	total += random.randrange(0, 999) + 1
	
print("The Average was", end = ' ')
print(format(total/k, "5.2f"), end = '.')