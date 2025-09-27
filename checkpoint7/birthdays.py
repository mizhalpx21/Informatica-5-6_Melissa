birthdays = {
    "Renata": "March 29th",
    "Shensi": "March 9th",
    "Aileen": "October 1st"

}

name = input("Enter a name from the dictionary: ") 
if name in birthdays:
    print(f"{birthdays[name]} is the birthday of {name}.")

else:
    print(f"I do not have birthday information for {name}")
    new = input("When is his or her birthday? ")
    birthdays[f"{name}"] = new
    print(f"{new}")
    print("Birthday database updated.")
    

    
    
