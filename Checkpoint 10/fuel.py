def main():
    fuel = input("Enter how much fuel in fractions x/y do you have: ").split("/")
    print(fuel)

    num = int(fuel[0])
    print(num)
    nem = int(fuel[1])
    print(nem)

    percent= int(num/nem)*100
    print(f,percent)


main()
