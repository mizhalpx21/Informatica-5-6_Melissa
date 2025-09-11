my_list = [5, 2, 3, 1, 4]
greatest = max(my_list)  #Is to find the greatest value in the list
print("The greatest number in the list is:", greatest) 

smallest = min( my_list) #Is to find the smallest number in the list
print("The smallest number in the list is:", smallest)

list_sum = sum(my_list) #To sum all the numbers in the list
print("The sum of all numbers in the list is:", list_sum)

list_lenght = len(my_list) #To find the lenght of the list
print("This list has:", list_lenght, "elements.")

in_order = sorted(my_list) #Create a copy my_list and sort it
print(in_order)

def filter_price(price): #Define a function to the filtered_price function
    if (price > 400): #Setting the conditions to the filter_price
      return True
    else: 
       return False

item_price = [230, 400, 450, 350, 370] #Adding the value to the item_price
filtered_price = filter(filter_price, item_price) #Remove the numbers that are less than 400
print(list(filtered_price)) 


