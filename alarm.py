def main(): 
    is_armed = False
    notion_detected = True
    door_open = False
    is_afternoon = True
    display_alarm(is_armed, notion_detected, door_open, is_afternoon)

def display_alarm(is_armed, ms, door_open, an):
    if is_armed:
        if ms:
            print("INTRUDER!!!!")
        if door_open:
            print("Door is open")
    else:
        if an and ms:
            print("Welcome home! Turning the light on!")


main()
        
