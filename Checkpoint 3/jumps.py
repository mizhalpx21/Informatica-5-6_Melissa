def main():
    number = int(input("Please type in a number: "))
    start = 2

    while True:
        print (start)
        start += 2
        if number == start:
            print(number)
            break

main()