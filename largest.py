def main():
    list_length = int(input("Enter the length of a list: "))
    number_list = []
    
    for i in range(list_length):  
        list_element = int(input("Enter element:"))
        number_list.append(list_element)
    print(number_list)
    print(max(number_list))
    file = open("largest.txt", "a")
    file.write(f"{number_list}\n")
   # print(max(number_list("largest.txt")))


main()