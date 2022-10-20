from ur_remote.URRobot import URRobot

if __name__ == '__main__':
    robot1 = URRobot("172.31.0.101")
    print(robot1.Dashboard.connect())
    print(robot1.Dashboard.load("moveAToB"))
    print(robot1.Dashboard.powerOnRobotArm())
    print(robot1.Dashboard.brakeRelease())
    print(robot1.Dashboard.play())
    print(robot1.Dashboard.isRunning())
    print(robot1.Dashboard.getRobotMode())
    print(robot1.Dashboard.getLoadedProgram())
    print(robot1.Dashboard.popupDisplay("Test popup"))
