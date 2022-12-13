import socket
import struct
from ur_remote.PrimaryEnum import DataFormat
from ur_remote.PrimaryEnum import SizeFormat
from ur_remote.PrimaryEnum import MESSAGE_TYPE
from ur_remote.PrimaryEnum import ROBOT_STATE_PACKAGE_TYPE

PRIMARY_PORT = 30011


class Primary:
    """
    Create a communication using TCP/IP with the Primary Client.

    UR robot needs to be set in remote mode on the polyscope application.

    :param ipAddress: the ip address of the Universal Robot.
    :type ipAddress: string
    """

    def __init__(self, ipAddress):
        self.ipAddress = ipAddress
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.offset = 0

    def connect(self):
        """
        Connect to the Universal Robot primary Server

        :return: The status of the connection
        :rtype: string
        """

        return self.server.connect((self.ipAddress, PRIMARY_PORT))

    def __unpack(self, data, dataType, offset):
        unpacked_data = struct.unpack_from('!' + dataType, data, self.offset)[0]
        self.offset += offset
        return unpacked_data

    def __unpackString(self, data, size):
        unpacked_data = struct.unpack_from(('!%d' + DataFormat.STRING) % size, data, self.offset)[0]
        self.offset += size * SizeFormat.UNSIGNED_CHAR
        return unpacked_data

    def readPort(self):
        data = self.server.recv(4096)
        self.offset = 0

        if data:
            messageSize = self.__unpack(data, DataFormat.INT, SizeFormat.INT)
            messageType = self.__unpack(data, DataFormat.UNSIGNED_CHAR, SizeFormat.UNSIGNED_CHAR)
            if messageType == MESSAGE_TYPE.ROBOT_STATE:
                self.__readRobotState(data)
            elif messageType == MESSAGE_TYPE.ROBOT_MESSAGE:
                self.__readRobotMessage(data)

    def __readRobotState(self, data):
        packageSize = self.__unpack(data, DataFormat.INT, SizeFormat.INT)
        packageType = self.__unpack(data, DataFormat.UNSIGNED_CHAR, SizeFormat.UNSIGNED_CHAR)
        if packageType == ROBOT_STATE_PACKAGE_TYPE.ROBOT_MODE_DATA:
            self.__readRobotModeData(data)
        elif packageType == ROBOT_STATE_PACKAGE_TYPE.JOINT_DATA:
            self.__readJointData(data)
        elif packageType == ROBOT_STATE_PACKAGE_TYPE.TOOL_DATA:
            self.__readToolData(data)
        elif packageType == ROBOT_STATE_PACKAGE_TYPE.MASTERBOARD_DATA:
            self.__readMasterboardData(data)
        elif packageType == ROBOT_STATE_PACKAGE_TYPE.CARTESIAN_INFO:
            self.__readCartesianInfo(data)
        elif packageType == ROBOT_STATE_PACKAGE_TYPE.KINEMATICS_INFO:
            self.__readKinematicsInfo(data)
        elif packageType == ROBOT_STATE_PACKAGE_TYPE.CONFIGURATION_DATA:
            self.__readConfigurationData(data)
        elif packageType == ROBOT_STATE_PACKAGE_TYPE.FORCE_MODE_DATA:
            self.__readForceModeData(data)
        elif packageType == ROBOT_STATE_PACKAGE_TYPE.ADDITIONAL_INFO:
            self.__readAdditionalInfo(data)
        elif packageType == ROBOT_STATE_PACKAGE_TYPE.TOOL_COMM_INFO:
            self.__readToolCommInfo(data)
        elif packageType == ROBOT_STATE_PACKAGE_TYPE.TOOL_MODE_INFO:
            self.__readToolModeInfo(data)
        elif packageType == ROBOT_STATE_PACKAGE_TYPE.SINGULARITY_INFO:
            self.__readSingularityInfo(data)

    def __readRobotMessage(self, data):
        """timestamp = self.__unpack(data, DataFormat.UNSIGNED_LONG_LONG, SizeFormat.UNSIGNED_LONG_LONG)
        source = self.__unpack(data, DataFormat.UNSIGNED_CHAR, SizeFormat.UNSIGNED_CHAR)
        robotMessageType = self.__unpack(data, DataFormat.UNSIGNED_CHAR, SizeFormat.UNSIGNED_CHAR)
        if robotMessageType == 9:
            requestId = self.__unpack(data, DataFormat.UNSIGNED_INT, SizeFormat.UNSIGNED_INT)
            requestedType = self.__unpack(data, DataFormat.UNSIGNED_INT, SizeFormat.UNSIGNED_INT)
            warning = self.__unpack(data, DataFormat.BOOLEAN, SizeFormat.BOOLEAN)
            error = self.__unpack(data, DataFormat.BOOLEAN, SizeFormat.BOOLEAN)
            blocking = self.__unpack(data, DataFormat.BOOLEAN, SizeFormat.BOOLEAN)
            popupMessageTitleSize = self.__unpack(data, DataFormat.UNSIGNED_CHAR, SizeFormat.UNSIGNED_CHAR)
            popupMessageTitle = self.__unpackString(data, popupMessageTitleSize)
            popupTextMessage = self.__unpackString(data, 4)
        elif robotMessageType == 7:
            robotMessageCode = self.__unpack(data, DataFormat.INT, SizeFormat.INT)
            robotMessageArgument = self.__unpack(data, DataFormat.INT, SizeFormat.INT)
            robotMessageTitleSize = self.__unpack(data, DataFormat.UNSIGNED_CHAR, SizeFormat.UNSIGNED_CHAR)
            robotMessageTitle = self.__unpackString(data, robotMessageTitleSize)
            keyTextMessage = self.__unpackString(data, 8)"""

    def __readRobotModeData(self, data):
        timestamp = self.__unpack(data, DataFormat.UNSIGNED_LONG_LONG, SizeFormat.UNSIGNED_LONG_LONG)
        isRealRobotConnected = self.__unpack(data, DataFormat.BOOLEAN, SizeFormat.BOOLEAN)
        isRealRobotEnabled = self.__unpack(data, DataFormat.BOOLEAN, SizeFormat.BOOLEAN)
        isRobotPowerOn = self.__unpack(data, DataFormat.BOOLEAN, SizeFormat.BOOLEAN)
        isEmergencyStopped = self.__unpack(data, DataFormat.BOOLEAN, SizeFormat.BOOLEAN)
        isProtectiveStopped = self.__unpack(data, DataFormat.BOOLEAN, SizeFormat.BOOLEAN)
        isProgramRunning = self.__unpack(data, DataFormat.BOOLEAN, SizeFormat.BOOLEAN)
        isProgramPaused = self.__unpack(data, DataFormat.BOOLEAN, SizeFormat.BOOLEAN)
        robotMode = self.__unpack(data, DataFormat.UNSIGNED_CHAR, SizeFormat.UNSIGNED_CHAR)
        controlMode = self.__unpack(data, DataFormat.UNSIGNED_CHAR, SizeFormat.UNSIGNED_CHAR)
        targetSpeedFraction = self.__unpack(data, DataFormat.DOUBLE, SizeFormat.DOUBLE)
        speedScaling = self.__unpack(data, DataFormat.DOUBLE, SizeFormat.DOUBLE)
        targetSpeedFractionLimit = self.__unpack(data, DataFormat.DOUBLE, SizeFormat.DOUBLE)

    def __readJointData(self, data):
        pass

    def __readToolData(self, data):
        pass

    def __readMasterboardData(self, data):
        pass

    def __readCartesianInfo(self, data):
        pass

    def __readKinematicsInfo(self, data):
        pass

    def __readConfigurationData(self, data):
        pass

    def __readForceModeData(self, data):
        pass

    def __readAdditionalInfo(self, data):
        pass

    def __readToolCommInfo(self, data):
        pass

    def __readToolModeInfo(self, data):
        pass

    def __readSingularityInfo(self, data):
        pass



