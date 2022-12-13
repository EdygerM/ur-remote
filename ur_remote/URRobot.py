from ur_remote.Dashboard import RobotMode
from ur_remote.Dashboard import Dashboard
from ur_remote.Primary import Primary


class URRobot:
    """
    Create a communication using TCP/IP with the clients of a Universal Robot.

    UR robot needs to be set in remote mode on the polyscope application.

    :param ipAddress: the ip address of the Universal Robot..
    :type ipAddress: string
    """

    def __init__(self, ipAddress):
        self.ipAddress = ipAddress
        self.Dashboard = Dashboard(ipAddress)
        self.Primary = Primary(ipAddress)

        self.Dashboard.connect()
        self.Primary.connect()
        if not self.Dashboard.isInRemoteControl():
            raise Exception(self.Dashboard.getRobotModel() +
                            " is not in remote mode, switch the robot in remote control")

    def powerOn(self):
        self.Dashboard.powerOnRobotArm()
        while self.Dashboard.getRobotMode() != RobotMode.IDLE:
            self.Dashboard.getRobotMode()
        self.Dashboard.brakeRelease()
        while self.Dashboard.getRobotMode() != RobotMode.RUNNING:
            self.Dashboard.getRobotMode()

    def powerOff(self):
        self.Dashboard.powerOffRobotArm()

    def runProgram(self, programName):
        self.Dashboard.load(programName)
        if self.Dashboard.getRobotMode() != RobotMode.RUNNING:
            self.powerOn()
        self.Dashboard.play()
        while not self.Dashboard.isRunning():
            pass
        while self.Dashboard.isRunning():
            pass
