def main():
    password = input("Set a password: ")
    input("Press enter to long in.")
    check_password(password)

def check_password(password):
    guess=input("Guess the password: ")
    if password == guess:
        print("You knew the password!")

    if guess != password:
        print("Get away from the keyboard you imposter!")
    print("The program has ended")

main()
    