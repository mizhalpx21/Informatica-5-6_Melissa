universities = {
   "URN": {"carrers": 3,
        "cost" : 2755,
        "closest campus" : 24.9},
    "UACJ" : {"carrers": 8,
            "cost" : 3800,
            "closest campus" : 35.4},
    "La SALLE" : {
        "carrers" : 19,
        "cost" : 60000,
        "closest campus" : 319},
    "UT Paquime" : {
        "carrers" : 4,
        "cost" : 1800,
        "closest campus" : 16.8},
    "ELPAC" : {
        "carrers": 1,
        "cost" : 28000,
        "closest campus" : 318}
}

def main():

    clean_list = "\n".join(universities)
    print(f"Universities: {clean_list}")

    uni = input("Write the name of a University: ")
    while uni not in universities:
        uni = input("Not found. Try again: ")
    if uni == input().lower:
        print("Write it in upper case: ")


main()
 

