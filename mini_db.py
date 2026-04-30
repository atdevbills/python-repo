name = input("Enter your name >> ")
age = int(input("Enter your age >> "))

with open("users.txt", "a") as file:
	file.write(f"\nName : {name} | Age : {age}")

with open("users.txt", "r") as file:
	content = file.read()
	print(content)
