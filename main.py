from ur_remote.URRobot import URRobot

if __name__ == '__main__':
    robot1 = URRobot("172.31.0.101")
    print(robot1.Dashboard.connect())
    print(robot1.Primary.connect())