def character_counter(message, dictionary):
    for  character in message:
        dictionary.setdefault(character, 0) #If the character does not exist; it will add it to the dictionary with the value of 0, and if it exist it will saltarselo
        dictionary[character] += 1
    
    print(dictionary)
    print

message = input("Write a message: ")
dictionary = {} 
character_counter(message, dictionary)
# print(message[0])

