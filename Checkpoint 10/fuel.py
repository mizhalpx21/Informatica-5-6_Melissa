def main():
    fuel()

def fuel():
    condition = True
    while condition:
        try:
            fraction= input("Enter how much fuel as fraction x/y do you have: ").split("/") 
            num = int(fuel[0])
            dem = int(fuel[1])
            percentage= round((num/dem)*100)
            if percentage > 100:
                print("Invalid input. Fuel tank cannot be filled more than 100%.")
                percentage = "E"
            elif percentage >= 99:
                print("F")
                break #(condition = False)
            elif percentage <= 1:
                print("E")
                break
            else:
                print(f"The percent is: {percentage}%")
                break
        except (ZeroDivisionError, ImportError):
            print("Invalid fraction")
        except ValueError:
            print("Type a number")


















# def main():
#     fuel = input("Enter how much fuel as fraction x/y do you have: ").split("/")
#     print(fuel)

#     num = int(fuel[0])
#     dem = int(fuel[1])
#     percentage= round((num/dem)*100)
#     print(f"{percentage}%")

# while True:
#     if percentage <= 1:
#         percentage = "E"
#     elif percentage >= 99:
#         percentage = "F"
#     elif percentage > 100:
#         print("Invalid input")
#         print(percentage)




main()
