def main():                                          #Main function
     message = input("Write a message: ").lower()    #This is what the function is asking and will convert the message in lowercase
     encode_message(message)                         #This is to encode the message written for the user


def encode_message(text):                      #This is to encode the message from the main function
    alphabet = "abcdefghijklmnopqrstuvwxyz"    #This is the alphabet variable
    cipher = "zyxwvutsrqponmlkjihgfedcba"      #This is the cipher variable
    new_message = ""                           #This is the variable that stores the encode message
    i = 0                                      #This is to start the counter with 0
 
    while i < len(text):                           # This tells that the t
          char = text[i]                           #
          if char in alphabet:                     #
              cipher_index = alphabet.find(char)   #
              new_message += cipher[cipher_index]  #
          else:                                    #    
              new_message += char                  #
          i += 1                                   #
    print("Encoded message:" +new_message)         #
    
main()                                             #



   

