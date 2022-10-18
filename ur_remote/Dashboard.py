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
        :return: NO_CONTROLLER, DISCONNECTED, CONFIRM_SAFETY, BOOTING, POWER_OFF, POWER_ON, IDLE, BACKDRIVE, RUNNING
        :rtype: string
        """

        return self.__sendCommand("robotmode").replace('Robotmode:', '')

    def getLoadedProgram(self):
        """
        :return: path to loaded program file
        :rtype: string
        """

        message = self.__sendCommand("get loaded program")

        if message == "No program loaded":
            return message
        else:
            return message.replace('Loaded program:', '')

    def popupDisplay(self, popupMessage):
        """
        Display a popup message on the Teach pendant. The popup-text will be translated to the selected language, if the text exists in the language file

        :param popupMessage: Message displayed in the popup window
        :type popupMessage: string

        :return: "showing popup"
        :rtype: string
        """

        return self.__sendCommand("popup " + popupMessage)

    def popupClose(self):
        """
        close the current popup

        :return: "closing popup"
        :rtype: string
        """

        return self.__sendCommand("close popup")

    def addToLog(self, logMessage):
        """
        Adds log-message to the Log history

        :param logMessage: Message displayed in the popup window
        :type logMessage: string

        :return: "Added log message" Or "No log message to add"
        :rtype: string
        """

        return self.__sendCommand("addToLog " + logMessage)

    def isProgramSaved(self):
        """
        :return: save state of the active program
        :rtype: boolean
        """

        if self.__sendCommand("isProgramSaved")[0:4] == "true":
            return True
        else:
            return False

    def getProgramState(self):
        """
        :return: STOPPED, PLAYING, PAUSED
        :rtype: string
        """

        return self.__sendCommand("programState")

    def getPolyscopeVersion(self):
        """
        :return: Version of the Polyscope software
        :rtype: string
        """

        return self.__sendCommand("PolyscopeVersion")

    def setOperationalMode(self, operationalMode):
        """
        Controls the operational mode. See User manual for details. Warning: This functionality is intended for using e.g. Ethernet based Key Card Readers to switch operational modes. The device for switching operational mode should be placed in vicinity to the robot.

        :param operationalMode: manual or automatic
        :type operationalMode: string

        :return: operational mode status
        :rtype: string
        """

        return self.__sendCommand("set operational mode " + operationalMode)

    def getOperationalMode(self):
        """
        Returns the operational mode as MANUAL or AUTOMATIC if the password has been set for Mode in Settings. Returns NONE if the password has not been set.

        :return: MANUAL, AUTOMATIC, NONE
        :rtype: string
        """

        return self.__sendCommand("get operational mode")

    def clearOperationalMode(self):
        """
        If this function is called the operational mode can again be changed from PolyScope, and the user password is enabled.

        :return: "operational mode is no longer controlled by Dashboard Server"
        :rtype: string
        """

        return self.__sendCommand("clear operational mode")

    def powerOnRobotArm(self):
        """
        :return: "Powering on"
        :rtype: string
        """

        return self.__sendCommand("power on")

    def powerOffRobotArm(self):
        """
        :return: "Powering on"
        :rtype: string
        """

        return self.__sendCommand("power off")

    def brakeRelease(self):
        """
        :return: "Brake releasing"
        :rtype: string
        """

        return self.__sendCommand("brake release")

    def getSafetyStatus(self):
        """
        :return: NORMAL, REDUCED PROTECTIVE_STOP, RECOVERY SAFEGUARD_STOP, SYSTEM_EMERGENCY_STOP, ROBOT_EMERGENCY_STOP, VIOLATION, FAULT, AUTOMATIC_MODE_SAFEGUARD_STOP, SYSTEM_THREE_POSITION_ENABLING_STOP
        :rtype: string
        """

        return self.__sendCommand("safetystatus")

    def UnlockProtectiveStop(self):
        """
        Closes the current popup and unlocks protective stop. The unlock protective stop command fails if less than 5 seconds has passed since the protective stop occurred.

        :return: unlock status
        :rtype: string
        """

        return self.__sendCommand("unlock protective stop")












