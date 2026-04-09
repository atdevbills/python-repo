fruits = ["mango", "orange", "pineapple", "banana"]

# Adding items
fruits.append("strawberry")      # add to end
fruits.insert(1, "watermelon")   # add at position 1
print(f"After adding: {fruits}")

# Removing items
fruits.remove("orange")          # remove by name
fruits.pop()                     # remove last item
print(f"After removing: {fruits}")

# Updating items
fruits[0] = "grape"
print(f"After updating: {fruits}")

# Looping through a list
print("\nAll fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# Checking if item exists
if "mango" in fruits:
    print("\nMango is in the list!")
else:
    print("\nMango is not in the list!")

# Sorting
fruits.sort()
print(f"\nSorted: {fruits}")
