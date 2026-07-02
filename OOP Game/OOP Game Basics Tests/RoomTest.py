import unittest
from Room import *
from GameObject import *


class RoomTest(unittest.TestCase):
    dummyRoom = Room(123, [GameObject(
        "Sweater",
        "It's a blue sweater that had the number 12 stitched on it.",
        "Someone has unstitched the second number, leaving only the 1.",
        "The sweater smells of laundry detergent."),
      GameObject(
        "Chair",
        "It's a wooden chair with only 3 legs.",
        "Someone had deliberately snapped off one of the legs.",
        "It smells like old wood.")])

    emptyRoom = Room(456, [])

    def test_check_code(self):
        self.assertTrue(self.dummyRoom.check_code(123))
        self.assertFalse(self.dummyRoom.check_code(222))

    def test_get_object_names(self):
        self.assertEqual(self.emptyRoom.get_game_object_names(), [])
        self.assertEqual(self.dummyRoom.get_game_object_names(), ["Sweater", "Chair"])