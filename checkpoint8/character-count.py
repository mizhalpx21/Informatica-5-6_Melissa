def character_counter(message, dictionary):
    for  character in message:
        dictionary.setdefault(character, 0) #If the character does not exist; it will add it to the dictionary with the value of 0, and if it exist it will saltarselo
        dictionary[character] += 1
    
    print(dictionary)
    # print(len(dictionary)) 
    print(f"Total character: {sum(dictionary.values())}")

    #Alternative 1
    values_list = list(dictionary.values())     #Use the values and turn them into a list, then store them in a list        
    print(values_list)
    largest_number_index = values_list.index(max(values_list))
    repeated_character = list(dictionary.keys())[largest_number_index]  #Create a list with keys and then it will look for the same index in the square brakets
    print(f"Most repeated character is: {largest_number_index}, repeating {dictionary[repeated_character]} times.")


    #Alternative 2
    largest_number_2 = max(dictionary, key = dictionary.get)
    print(f"Most repeated character is: {largest_number_2}, repeating {dictionary[largest_number_2]} times.")




message = input("Write a message: ")
dictionary = {} 
character_counter(message, dictionary)
# print(message[0])
