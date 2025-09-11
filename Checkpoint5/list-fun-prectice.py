def main():
   print(lenght(values()))
   mean(values())
   range_list(values())

def values():
    value_list = []
    while True:
        value = int(input("Enter a value: "))
        if value != 0:
            value_list.append(value)
            print(value_list)
            ordered_list = sorted(value_list)
            print(ordered_list)
            continue
        else:
            break
    return value_list

def lenght(list):
    return len(list)

def mean(list):
    print(sum(list) / len(list))

def range_list(list):
    print(max(list) - min(list))
 
main()

 