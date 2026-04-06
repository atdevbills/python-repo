def greet(name):
    print(f"Hello {name}, welcome!")

def add(num1, num2):
    return num1 + num2

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

# Now use them
greet("Baanbil")

result = add(10, 20)
print(f"10 + 20 = {result}")

age = 19
if is_adult(age):
    print(f"{age} years old is an adult!")
else:
    print(f"{age} years old is not an adult!")
