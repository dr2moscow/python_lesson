num = input("Enter number: ")
try:
	num = int(num)
	print(num)
except ValueError:
	print("Error")