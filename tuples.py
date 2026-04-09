# Creating a tuple
months = ("January", "February", "March", "April",
          "May", "June", "July", "August",
          "September", "October", "November", "December")

# Accessing items
print(months[0])       # first month
print(months[-1])      # last month
print(len(months))     # number of months

# Looping through tuple
print("\nAll months:")
for month in months:
    print(f"  - {month}")

# Checking if item exists
if "March" in months:
    print("\nMarch is a valid month!")

# Tuple unpacking
coordinates = (5.6037, 0.1870)
latitude, longitude = coordinates
print(f"\nGhana Coordinates:")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
