#Dictionary 
#word: meaning
#key: value

capitals = {                      #Making a dictionary
    "Mexico": "Mexico City",      #Adding the capital of the country form 3 to 5
    "Canada":"Ottawa",
    "Brazil": "Brasilia"
    #"Canada":"Ottawa"     Use unique keys
}

capitals["Italy"] = "Rome" #This is to add an element to the dictionary
del capitals["Brazil"]    #Deleate key and its word
capitals.pop("Canada")   #Another way to deleate a key and its word
capitals.clear()        #Clears the dictionary
#print(capitals) To print the dictionary
#print(capitals["Canada"]) Printing a specific capital of a key


houses ={                            #Making a dictionary
    "Hermione": "Gryffindor",        #Writing the house to the student from 21 to 24
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# for key in houses:     #Para cada key en el diccionarios llamado houses vas a...
#     print(f"{key}: {houses[key]}") #Print the key that will be the house of the key

students =[
    
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for element in students:
    print(f"{element["name"]}, {element["house"]}, {element["patronus"]}")