from ur_remote.Dashboard import Dashboard
from ur_remote.Primary import Primary


class URRobot:
    """
    Create a communication using TCP/IP with the clients of a Universal Robot.

    UR robot needs to be set in remote mode on the polyscope application.

    :param ipAddress: the ip address of the Universal Robot.
    :type ipAddress: string
    """

    def __init__(self, ipAddress):
        self.ipAddress = ipAddress
        self.Dashboard = Dashboard(ipAddress)
        self.Primary = Primary(ipAddress)
