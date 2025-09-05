def main():
    positive_integer_number = int(input("Write a positive integer number from 1 to 10: "))
    multiplication( positive_integer_number)

def multiplication(positive_integer_number):
    n = 1
    positive_integer_number == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10

    while n<= 10:
        if positive_integer_number > 0:
            ans = positive_integer_number * n
            print(f"{positive_integer_number} x {n} = {ans}")
            n += 1
        else:
            print("Try again")
            positive_integer_number = int(input("Write a positive integer number from 1 to 10: "))
    

main()
    
        

    
     



