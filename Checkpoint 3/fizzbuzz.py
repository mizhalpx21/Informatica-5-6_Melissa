def main():
    integer_number =int(input("Type an integer number: "))
    if integer_number % 3 == 0 and integer_number % 5 == 0:
        print("FizzBuzz") 
    elif integer_number % 5 == 0:
        print("Buzz")
    elif  integer_number % 3 == 0:
        print ("Fizz")


main()
