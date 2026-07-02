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


def interact_with_object(obj, interaction):
    match interaction:
        case 1:
            return obj.look()
        case 2:
            return obj.touch()
        case 3:
            return obj.sniff()
        case _:
            return "Invalid choice!"


def get_object_interaction_string(name):
    return (f"How do you want to interact with the {name}?\n"
            f"1. Look\n2. Touch\n3. Smell\n")


class Game:
    def __init__(self):
        self.attempts = 0
        self.room = Room(731, create_objects())

    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = int(input(prompt))
        if 1 <= selection <= 5:
            self.select_object(selection-1)
            self.take_turn()
        elif selection <= 0:
            print("Goodbye!")
            return
        else:
            if self.guess_code(selection):
                print("Congratulations! You win!")
            else:
                if self.attempts == 3:
                    print("LOSER")
                else:
                    print(f"Incorrect choice! You have {3-self.attempts} attempts remaining!")
                    self.take_turn()

    def get_room_prompt(self):
        prompt = "Enter the 3 digit lock code or choose an item to interact with:\n"
        names = self.room.get_game_object_names()
        index = 1
        for name in names:
            prompt += f"{index}: {name}\n"
            index += 1
        return prompt

    def select_object(self, index):
        selected_object = self.room.game_objects[index]
        prompt = get_object_interaction_string(selected_object.name)
        interaction = int(input(prompt))
        print(interact_with_object(selected_object, interaction))
        return

    def guess_code(self, guess):
        if self.room.check_code(guess):
            return True
        else:
            self.attempts += 1
            return False