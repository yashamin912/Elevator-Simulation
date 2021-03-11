import multiprocessing
import time


class Elevator:
    def __init__(self, button,):
        self.button = button
        self.opener = 'o'

    def open_close(self, slider):

        if slider == self.opener:
            if slider == 'o':
                return f"The Doors are already open."
            elif slider == 'c':
                return f"The Doors are already closed."
        elif slider != self.opener:
            self.opener = slider
            if slider == 'c':
                return "Doors are closing."
            elif slider == 'o':
                return "Doors are opening."


    def floor_selection(self, new_floor):
        place_holder = self.button
        self.button = new_floor
        if self.opener == 'o':
            print("\nDoors are closing.")
        self.opener = 'o'
        return f"You are on floor {place_holder} and going to {new_floor}.\nThe doors have opened."

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


    print(f"Here is the button list: {button_list}\nfa = fire alarm \no = open door \nc = close door")
    button = input("Welcome to our elevator! The Doors have opened. Awaiting input... (type 's' to end.) ")
    Person = Elevator(floor)

    while button != "s":
        while button not in button_list:
            button = input("Please put in a actual input. Waiting for input... ")

        if button in floor_list:
            if button == floor:
                print(f"\nYou're already on that floor")
            else:
                print(f"\n{Person.floor_selection(button)}")
                floor = Person.button

        elif button in Operation_list:
            if button == 'fa':
                print(f"\n{Person.fire_alarm()}")
            elif button in 'oc':
                print(f"\n{Person.open_close(button)}")
        button = input("Anything else? Awaiting input... (type 's' to end.) ")
    print("Bye bye")


user_inputs(current_floor)




