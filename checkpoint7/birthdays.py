birthdays = [
    {"name": "Renata", "birthday": "March 29th"},
    {"name": "Shensi", "birthday": "March 9th"},
    {"name": "Aileen", "birthday": "October 1st"}

]

name = input("Enter a name from the dictionary: ") 

if name in birthdays:
    print(f"{name}: {name[name]}, {birthday}:")