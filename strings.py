name = "baanbil atdevbills"

# Capitalization
print(name.upper())          # BAANBIL ATDEVBILLS
print(name.lower())          # baanbil atdevbills
print(name.title())          # Baanbil Atdevbills
print(name.capitalize())     # Baanbil atdevbills

# Searching
print(name.find("at"))       # position of "at"
print(name.count("a"))       # count letter "a"
print(name.startswith("ba")) # True or False
print(name.endswith("ls"))   # True or False

# Replacing
print(name.replace("atdevbills", "github"))

# Splitting
words = name.split(" ")      # split into list
print(words)

# Stripping whitespace
messy = "   hello world   "
print(messy.strip())         # removes spaces

# Checking content
print("12345".isdigit())     # True
print("hello".isalpha())     # True
print("hello123".isalnum())  # True

# Length
print(len(name))             # number of characters
