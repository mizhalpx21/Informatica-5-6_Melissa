def main():
    name = input("Enter your name: ")
    coke = 50
    coin = int(input("Insert a coin (one at a time): "))
    
    while coin == 25 or coin ==10 or coin == 5:
        print("Here is your change: {coke - coin}")
        if coin != 25 and coin == 10 and coin == 5:
            print("Not the correct coin")
        


main()