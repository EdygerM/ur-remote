from ur_remote.URRobot import URRobot

if __name__ == '__main__':
    robot1 = URRobot("172.31.0.101")
    print(robot1.Dashboard.connect())
    print(robot1.Dashboard.load("MoveAToB"))
    print(robot1.Dashboard.isRunning())
    print(robot1.Dashboard.getRobotMode())
    print(robot1.Dashboard.getLoadedProgram())
    print(robot1.Dashboard.popupDisplay("Test popup"))