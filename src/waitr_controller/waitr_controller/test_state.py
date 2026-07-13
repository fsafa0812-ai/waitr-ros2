from state_machine import StateMachine, RobotState

robot = StateMachine()

robot.change_state(RobotState.GO_TO_KITCHEN)
robot.change_state(RobotState.PICK_FOOD)
robot.change_state(RobotState.GO_TO_TABLE)
robot.change_state(RobotState.DELIVER_FOOD)
