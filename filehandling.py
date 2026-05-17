with open("data.txt", "w") as file:
	file.write("Hello World")

with open("data.txt", "a") as file:
	file.write("\nHow are you doing?\nWhat's your name?")

with open("data.txt", "r") as file:
	content = file.read()
	print(content)
