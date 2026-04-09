student = {
    "name": "Baanbil",
    "age": 19,
    "country": "Ghana",
    "course": "AI & Machine Learning"
}

# Accessing values
print(student["name"])
print(student["age"])

# Adding a new key
student["github"] = "atdevbills"
print(f"\nUpdated: {student}")

# Updating a value
student["age"] = 20
print(f"Age updated: {student['age']}")

# Removing a key
del student["course"]
print(f"After delete: {student}")

# Looping through dictionary
print("\nStudent Info:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Check if key exists
if "github" in student:
    print(f"\nGitHub: {student['github']}")
