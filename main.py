import time
from ur_remote.URRobot import URRobot

if __name__ == '__main__':
    robot = URRobot("192.168.0.21")
    robot.Primary.readPort()
    # robot.runProgram("moveAToB")
    # robot.runProgram("moveBToC")
    # robot.runProgram("moveCToA")
    # robot.powerOff()
