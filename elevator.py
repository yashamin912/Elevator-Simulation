import multiprocessing
import time
class Elevator:
    def __init__(self, floor):
        self.floor = floor

    def open_door(self):
        return "The door has opened"

    def close_door(self):
        return "The door has closed"

    def floor_selection(self, new_floor):
        place_holder = self.floor
        self.floor = new_floor

        print("The door are closing")

        return f"You are on floor {place_holder} and going to {new_floor}.\nThe door has opened."



    def fire_alarm(self):
        return "DING DING DING"




"""Ask user what do they want to do inside the elevator"""
button_list = ["1", "2", "3", "4", "5", "6", "7", "fa", "o", "c"]
floor_list = button_list[0:7]
Operation_list = button_list[-3:]
current_floor = input("What floor are you on? (Floors: 1-7) ")


def user_inputs(floor):
    if floor not in floor_list:
        while floor not in floor_list:
            floor = input("Please type as integer and make sure it's in range. (Floors: 1-7) ")
    Person = Elevator(floor)
    print(f"Here is the button list: {button_list}")
    button = input("Welcome to our elevator! Waiting for input... (type 's' to end.) ")
    while button != "s":
        while button not in button_list:
            button = input("Please put in a actual input. Waiting for input... ")


        if button in floor_list:
            if button == floor:
                print(f"\nYou're already on that floor")
            else:
                print(f"\n{Person.floor_selection(button)}")
                floor = Person.floor

        elif button in Operation_list:
            if button == 'fa':
                print(f"\n{Person.fire_alarm()}")
            elif button == 'c':
                print(f"\n{Person.close_door()}")
            elif button == 'o':
                print(f"\n{Person.open_door()}")
        button = input("Anything else? Waiting for input... (type 's' to end.) ")
    print("Bye bye")


user_inputs(current_floor)
