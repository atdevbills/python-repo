num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
print("Select your operation\n1.+\n2.*\n3.-\n4./")
op = int(input(">>> "))
print("======================")
if op == 1:
	print(num1 + num2)
elif op == 2:
	print(num1 * num2)
elif op == 3:
	print(num1 - num2)
elif op == 4:
	if num2 == 0:
		print("cannot divide by zero")
	else:
		print(num1 / num2)
else:
	print("please select a number")
