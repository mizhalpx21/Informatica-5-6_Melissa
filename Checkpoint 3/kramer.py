while True:
     greeting = input("Write a greeting: ")
     if greeting.startswith("hello"):
             print("You have received $0")    
     elif greeting.startswith("h"):
            print("You have received $20")
     else:
       print("You have received $100")
       break


