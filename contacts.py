import json

contacts = [
    {"name": "Baanbil", "phone": "024xxxxxxx"},
    {"name": "Mildred", "phone": "055xxxxxxx"}
]

with open("contacts.json", "w") as file:
    json.dump(contacts, file)

with open("contacts.json", "r") as file:
    saved = json.load(file)

for contact in saved:
    print(f"{contact['name']} - {contact['phone']}")
