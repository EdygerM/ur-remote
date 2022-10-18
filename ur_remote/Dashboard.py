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

    def __sendCommand(self, command):
        """
        Send a command to the client, then read its feedback

        :param command: command sent to the Dashboard Server
        :type command: string

        :return: The message sent by the client depending on the command
        :rtype: string
        """
        self.server.sendall(command.encode())
        message = self.server.recv(1024)

        return message.decode()

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

        return self.__sendCommand("load " + programName + ".urp\n")

    def play(self):
        """
        Play the program loaded

        :return: Returns failure if the program fails to start.
        :rtype: string
        """

        return self.__sendCommand("play")

    def stop(self):
        """
        Stop the program loaded

        :return: Returns failure if the program fails to stop.
        :rtype: string
        """

        return self.__sendCommand("stop")

    def pause(self):
        """
        Pause the program loaded

        :return: Returns failure if the program fails to pause.
        :rtype: string
        """

        return self.__sendCommand("pause")

    def quit(self):
        """
        Closes connection

        :return: "Disconnected"
        :rtype: string
        """

        return self.__sendCommand("quit")

    def shutdown(self):
        """
        Shuts down and turns off robot and controller.

        :return: "Shutting down"
        :rtype: string
        """

        return self.__sendCommand("shutdown")

    def isRunning(self):
        """
        Execution state enquiry

        :return: running state
        :rtype: boolean
        """

        if self.__sendCommand("running") == "Program running: true":
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
        message = self.server.recv(1024)

        return message.decode().replace('Robotmode:', '')

    def getLoadedProgram(self):
        """
        Which program is loaded

        :return: path to loaded program file
        :rtype: string
        """

        call = "get loaded program"
        self.server.sendall(call.encode())
        message = self.server.recv(1024)
        if message.decode() == "No program loaded":
            return message.decode()
        else:
            return message.decode().replace('Loaded program:', '')

    def popupDisplay(self, popupMessage):
        """
        Display a popup message on the Teach pendant. The popup-text will be translated to the selected language, if the text exists in the language file

        :param popupMessage: Message displayed in the popup window
        :type popupMessage: string

        :return: "showing popup"
        :rtype: string
        """

        call = "popup " + popupMessage
        self.server.sendall(call.encode())

        return self.server.recv(1024)

    def popupClose(self):
        """
        close the current popup

        :return: "closing popup"
        :rtype: string
        """

        call = "close popup"
        self.server.sendall(call.encode())

        return self.server.recv(1024)

    def addToLog(self, logMessage):
        """
        Adds log-message to the Log history

        :param logMessage: Message displayed in the popup window
        :type logMessage: string

        :return: "Added log message" Or "No log message to add"
        :rtype: string
        """

        call = "addToLog " + logMessage
        self.server.sendall(call.encode())

        return self.server.recv(1024)

    def isProgramSaved(self):
        """
        Returns the save state of the active program

        :return: save state
        :rtype: boolean
        """

        call = "isProgramSaved"
        self.server.sendall(call.encode())
        message = self.server.recv(1024)

        if message.decode()[0:4] == "true":
            return True
        else:
            return False

    def getProgramState(self):
        """
        Program State enquiry

        :return: STOPPED, PLAYING, PAUSED
        :rtype: string
        """

        call = "programState"
        self.server.sendall(call.encode())
        message = self.server.recv(1024)

        return message.decode()

    def getPolyscopeVersion(self):
        """
        :return: Version of the Polyscope software
        :rtype: string
        """

        call = "PolyscopeVersion"
        self.server.sendall(call.encode())
        message = self.server.recv(1024)

        return message.decode()







