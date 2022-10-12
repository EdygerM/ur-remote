import socket

DASHBOARD_PORT = 29999


class URDashboard:
    """
    Create a communication using TCP/IP with the dashboard server interface of a Universal Robot e-series.
    Based on https://www.universal-robots.com/articles/ur/dashboard-server-e-series-port-29999/ as of 07.10.22
    UR robot needs to be set in remote mode on the polyscope application.
    :param ipAddress: the ip address of the Universal Robot.
    :type ipAddress: string
    """

    def __init__(self, ipAddress):
        self.ipAddress = ipAddress
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Connect to the Universal Robot dashboard Server
        :return: The status of the connection
        :rtype: string
        """

        self.server.connect((self.ipAddress, DASHBOARD_PORT))

        return self.server.recv(1024)

    def load(self, programName):
        """
        Load a myProgram.urp file already present on the robot.
        :param programName: name of the .urp program (without the .urp)
        :type programName: string

        :return:
        :rtype: string
        """
        call = "load " + programName + ".urp\n"
        self.server.sendall(call.encode())

        return self.server.recv(1024)