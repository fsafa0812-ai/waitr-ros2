from enum import Enum

class RobotState(Enum):
    IDLE = 1
    GO_TO_KITCHEN = 2
    PICK_FOOD = 3
    GO_TO_TABLE = 4
    DELIVER_FOOD = 5
    RETURN_TO_KITCHEN = 6
class StateMachine:
    def __init__(self):
        self.state = RobotState.IDLE

    def change_state(self, new_state):
    
        self.state = new_state
        print(f"WaitR State: {self.state.name}")
    def get_state(self):
        return self.state