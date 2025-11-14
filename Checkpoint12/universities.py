import requests
universities = {
   "URN": {"carrers": 3,
        "cost" : 2755,
        "closest campus" : "Nuevo Casas Grandes"},
    "UACJ" : {"carrers": 8,
            "cost" : 3800,
            "closest campus" : "Nuevo Casas Grandes"},
    "La SALLE" : {
        "carrers" : 19,
        "cost" : 60000,
        "closest campus" : "Chihuahua"},
    "UT PAQUIME" : {
        "carrers" : 4,
        "cost" : 1800,
        "closest campus" : "Nuevo Casas Grandes"},
    "ELPAC" : {
        "carrers": 1,
        "cost" : 28000,
        "closest campus" : "Chihuahua"}
}

def main():

    clean_list = "\n".join(universities)
    print(f"Universities: {clean_list}")

    uni = input("Write the name of a University: ").upper()
    while uni not in universities:
        uni = input("Not found. Try again: ")

    api= requests.get("http://universities.hipolabs.com/search?name="+universities[uni]["official_name"])
    print(api.json())
        

main()
 

