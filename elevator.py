class Elevator:
    def __init__(self, floor):
        self.floor = floor


    def open_door(self):
      """This opens the door"""
      return ("The door has opened")

    def close_door(self):
      """This closes the door"""
      return ("The door has closed")

    def floor_selection(self, new_floor):
      """This transports you from current floor to your floor selection."""
      place_holder = self.floor
      self.floor = new_floor
      print("The door are closing")
      
      return f"You are on floor {place_holder} and going to {new_floor}."

    def fire_alarm(self):
      """This sounds the fire alarm"""
      return "DING DING DING"


"""List of buttons for the user to choose from."""

button_list = ["1", "2", "3", "4", "5", "6", "7", "fa", "o", "c"]
floor_list = button_list[0:7]
Operation_list = button_list[-3:]


"""Asks what floor the User is on."""

current_floor = input("What floor are you on? (Floors: 1-7) ")
if current_floor not in button_list:
    while current_floor not in button_list:
        current_floor = input("Please type as integer and make sure it's in range. (Floors: 1-7) ")
Person = Elevator(current_floor)

"""Ask user what do they want to do inside the elevator"""

print(f"Here is the button list: {button_list}")
button = input("Welcome to our elevator! Waiting for input... (type 's' to end.) ")


"""Loops until the person is done with elevator"""

while button != "s":
    if button not in button_list:
        while button not in button_list:
            button = input("Please put in a actual input. Waiting for input... ")
    elif button in floor_list:
        if button == current_floor:
            print("You're already on that floor")
        else:
            print(Person.floor_selection(button))
            current_floor = Person.floor

    elif button in Operation_list:
        if button == 'fa':
            print(Person.fire_alarm())
        elif button == 'c':
            print(Person.close_door())
        elif button == 'o':
            print(Person.open_door())
    button = input("Anything else? Waiting for input... (type 's' to end.) ")
print("Bye bye")
