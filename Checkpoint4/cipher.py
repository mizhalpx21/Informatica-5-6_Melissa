def main():                                          #Main function
     message = input("Write a message: ").lower()    #This is what the function is asking and will convert the message in lowercase
     encode_message(message)                         #This is to encode the message written for the user


def encode_message(text):                      #This is to encode the message from the main function
    alphabet = "abcdefghijklmnopqrstuvwxyz"    #This is the alphabet variable
    cipher = "zyxwvutsrqponmlkjihgfedcba"      #This is the cipher variable
    new_message = ""                           #This is the variable that stores the encode message
    i = 0                                      #This is to start the counter with 0
 
    while i < len(text):                           #This loop goes through each character of the message to apply the encoding process 
          char = text[i]                           #This is to get the current character
          if char in alphabet:                     #Checks if the character is in the alphabet
              cipher_index = alphabet.find(char)   #This finds the position of the letter in the alphabet
              new_message += cipher[cipher_index]  #This replace the letter with the corresponding letter in the cipher alphabet
          else:                                    #This is to decide what to do if the condition is false
              new_message += char                  #It leaves the character as it is if it is not a letter 
          i += 1                                   #Tells the index to move to the next character by incrementing it
    print("Encoded message:" +new_message)         #This is to print the encode message
    
main()                                             #This is to run the function



   

