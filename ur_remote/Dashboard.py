import socket
import time

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
        self.server.send(command.encode())

        time.sleep(1)

        return self.server.recv(4096).decode()

    def connect(self):
        """
        Connect to the Universal Robot dashboard Server

        :return: The status of the connection
        :rtype: string
        """

        self.server.connect((self.ipAddress, DASHBOARD_PORT))

        return self.server.recv(1024).decode()

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

    def unlockProtectiveStop(self):
        """
        Closes the current popup and unlocks protective stop. The unlock protective stop command fails if less than 5 seconds has passed since the protective stop occurred.

        :return: unlock status
        :rtype: string
        """

        return self.__sendCommand("unlock protective stop")

    def closeSafetyPopup(self):
        """
        :return: "closing safety popup"
        :rtype: string
        """

        return self.__sendCommand("close safety popup")

    def loadInstallation(self, installationName):
        """
        Loads the specified installation file but does not return until the load has completed (or failed).
        The load command fails if the associated installation requires confirmation of safety.
        The return value will be 'Failed to load installation'.

        :param installationNameName: name of the .installation program (without the .installation)
        :type installationNameName: string

        :return: loading status
        :rtype: string
        """

        return self.__sendCommand("load " + installationNameName + ".installation\n")

    def restartSafety(self):
        """
        Used when robot gets a safety fault or violation to restart the safety.
        After safety has been rebooted the robot will be in Power Off.
        IMPORTANT: You should always ensure it is okay to restart the system.
        It is highly recommended to check the error log before using this command (either via PolyScope or e.g. ssh connection).

        :return: "Restarting status"
        :rtype: string
        """

        return self.__sendCommand("restart safety")

    def isInRemoteControl(self):
        """
        :return: remote control status
        :rtype: boolean
        """

        if self.__sendCommand("is in remote control") == "true":
            return True
        else:
            return False

    def getSerialNumber(self):
        """
        :return: Serial number like "20175599999"
        :rtype: string
        """

        return self.__sendCommand("get serial number")

    def getRobotModel(self):
        """
        :return: UR3, UR5, UR10, UR16
        :rtype: string
        """

        return self.__sendCommand("get robot model")

    def generateFlightReport(self, reportType):
        """
        Triggers a Flight Report of the following type:
        • Controller - report with information specific for diagnosing controller errors. For example, in case of protective stops, faults or violations.
        • Software - report with information specific for polyscope software failures.
        • System - report with information about robot configuration, programs, installations, etc.
        It is required to wait at least 30 seconds between triggering software or controller reports.

        :param reportType: controller, software, system
        :type reportType: string

        :return: On success report id is printed. Error Message on a failure. Command can take few minutes to complete.
        :rtype: string
        """

        return self.__sendCommand("generate flight report " + reportType)

    def generateSupportFile(self, directoryPath):
        """
        Generates a flight report of the type "System" and creates a compressed collection of all the existing flight reports on the robot along with the generated flight report.
        Result file ur_[robot serial number]_YYYY-MM-DD_HHMM-SS.zip is saved inside <Directory path>

        :param directoryPath:
        :type directoryPath: string

        :return: On success "Completed successfully: <result file name>" is printed otherwise an error message with possible cause of the error is shown.
        Command can take up to 10 minutes to complete.
        :rtype: string
        """

        return self.__sendCommand("generate support file " + directoryPath)










