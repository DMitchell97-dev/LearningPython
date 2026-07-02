from Room import *
from GameObject import *

#Static
def create_objects():
    return [
      GameObject(
        "Sweater",
        "It's a blue sweater that had the number 12 stitched on it.",
        "Someone has unstitched the second number, leaving only the 1.",
        "The sweater smells of laundry detergent."),
      GameObject(
        "Chair",
        "It's a wooden chair with only 3 legs.",
        "Someone had deliberately snapped off one of the legs.",
        "It smells like old wood."),
      GameObject(
        "Journal",
        "The final entry states that time should be hours then minutes then seconds (H-M-S).",
        "The cover is worn and several pages are missing.",
        "It smells like musty leather."),
      GameObject(
        "Bowl of soup",
        "It appears to be tomato soup.",
        "It has cooled down to room temperature.",
        "You detect 7 different herbs and spices."),
      GameObject(
        "Clock",
        "The hour hand is pointing towards the soup, the minute hand towards the chair, and the second hand towards the sweater.",
        "The battery compartment is open and empty.",
        "It smells of plastic."),
    ]


class Game:
    def __init__(self):
        self.attempts = 0
        self.room = Room(731, create_objects())

    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = input(prompt)
        print(selection)

    def get_room_prompt(self):
        prompt = "Enter the 3 digit lock code or choose an item to interact with:\n"
        names = self.room.get_game_object_names()
        index = 1
        for name in names:
            prompt += f"{index}: {name}\n"
            index += 1
        return prompt
