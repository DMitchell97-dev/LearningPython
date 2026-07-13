class ParkingSystem:
    def __init__(self, big:int, medium:int, small:int):
        self.available_slots = [big, medium, small]

    def add_car(self, veh_type: int) -> bool:
        if self.available_slots[veh_type-1] > 0:
            self.available_slots[veh_type-1] -= 1
            return True
        else:
            return False
