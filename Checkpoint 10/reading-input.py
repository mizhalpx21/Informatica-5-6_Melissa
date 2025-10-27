def main():
  number = read_input("Please type in a number: ", 5, 10)
  print("You typed in:", number)

def read_input(prompt, small, large): # Insert missing parameters
    try:
        x = int(input(prompt)) # Complete the program here
        if 5 < x < 10:
           return x
        else:
            print("Please type a number BETWEEN", small, "and", large) 
    except ValueError:
       print("Please type a NUMBER between", small, "and", large) #the plus sign is to conctanate the numbers

main()