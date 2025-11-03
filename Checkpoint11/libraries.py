# import random

# coin = random.choice(["heads", "tails"])     #Chooses between a list
# print(coin)

# number = random.randint(1,10)
# print(number)

# cards = ["jacks", "queen", "king", "Ace"]
# random.shuffle(cards)                   #Varajea al azar
# for card in cards:
#     print(card)

# import statistics
# print(statistics.mean([100,90])) #Prints the mean of 100 plus 90
# print(statistics)

import cowsay
import sys
try:
    cowsay.cow("Hello, my name is", sys.argv[1])   #An argument is what is inside the quotation marks
except IndexError:
 #   print("Too few arguments")
    sys.exit()

# import statistics
# import sys    #Access library
# print(statistics.mean([int(sys.argv[1]), int(sys.argv[2])]))   