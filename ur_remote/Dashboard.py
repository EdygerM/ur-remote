import socket

DASHBOARD_PORT = 29999


class Dashboard:
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

        :return: Returns when both program and associated installation has loaded (or failed). The load command fails if the associated installation requires confirmation of safety. The return value in this case will be 'Error while loading program.
        :rtype: string
        """

        call = "load " + programName + ".urp\n"
        self.server.sendall(call.encode())

        return self.server.recv(1024)

    def play(self):
        """
        Play the program loaded

        :return: Returns failure if the program fails to start.
        :rtype: string
        """

        call = "play"
        self.server.sendall(call.encode())

        return self.server.recv(1024)

    def stop(self):
        """
        Stop the program loaded

        :return: Returns failure if the program fails to stop.
        :rtype: string
        """

        call = "stop"
        self.server.sendall(call.encode())

        return self.server.recv(1024)

    def pause(self):
        """
        Pause the program loaded

        :return: Returns failure if the program fails to pause.
        :rtype: string
        """

        call = "pause"
        self.server.sendall(call.encode())

        return self.server.recv(1024)

    def quit(self):
        """
        Closes connection

        :return: "Disconnected"
        :rtype: string
        """

        call = "quit"
        self.server.sendall(call.encode())

        return self.server.recv(1024)

    def shutdown(self):
        """
        Shuts down and turns off robot and controller.

        :return: "Shutting down"
        :rtype: string
        """

        call = "shutdown"
        self.server.sendall(call.encode())

        return self.server.recv(1024)

    def isRunning(self):
        """
        Execution state enquiry

        :return: running state
        :rtype: boolean
        """

        call = "running"
        self.server.sendall(call.encode())
        message = self.server.recv(1024)

        if message.decode() == "Program running: true":
            return True
        else:
            return False

    def getRobotMode(self):
        """
        Robot mode enquiry

        :return: NO_CONTROLLER, DISCONNECTED, CONFIRM_SAFETY, BOOTING, POWER_OFF, POWER_ON, IDLE, BACKDRIVE, RUNNING
        :rtype: string
        """

        call = "running"
        self.server.sendall(call.encode())
        message = self.server.recv(1024);

        robotMode = message.decode().replace('Robotmode:', '')

        return robotMode
