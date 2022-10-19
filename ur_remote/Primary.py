import socket
import struct
from ur_remote.PrimaryEnum import DataFormat
from ur_remote.PrimaryEnum import SizeFormat
from ur_remote.PrimaryEnum import MessageType


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

    def readPort(self):
        """

        """

        data = self.server.recv(4096)
        self.offset = 0

        if data:
            messageSize = self.__unpack(data, DataFormat.INT, SizeFormat.INT)
            messageType = self.__unpack(data, DataFormat.UNSIGNED_CHAR, SizeFormat.UNSIGNED_CHAR)
            if messageType == MessageType.MESSAGE_TYPE_ROBOT_MESSAGE:
                timestamp = self.__unpack(data, DataFormat.UNSIGNED_LONG_LONG, SizeFormat.UNSIGNED_LONG_LONG)
                source = self.__unpack(data, DataFormat.UNSIGNED_CHAR, SizeFormat.UNSIGNED_CHAR)
                robotMessageType = self.__unpack(data, DataFormat.UNSIGNED_CHAR, SizeFormat.UNSIGNED_CHAR)
                print(ord(robotMessageType))
                if ord(robotMessageType) == 9:
                    requestId = self.__unpack(data, DataFormat.UNSIGNED_INT, SizeFormat.UNSIGNED_INT)
                    requestedType = self.__unpack(data, DataFormat.UNSIGNED_INT, SizeFormat.UNSIGNED_INT)
                    warning = self.__unpack(data, DataFormat.BOOLEAN, SizeFormat.BOOLEAN)
                    error = self.__unpack(data, DataFormat.BOOLEAN, SizeFormat.BOOLEAN)
                    blocking = self.__unpack(data, DataFormat.BOOLEAN, SizeFormat.BOOLEAN)
                    popupMessageTitleSize = self.__unpack(data, DataFormat.UNSIGNED_CHAR, SizeFormat.UNSIGNED_CHAR)
                    popupMessageTitle = struct.unpack_from('!%ds' % popupMessageTitleSize, data, offset)[0]
                    self.offset += popupMessageTitleSize
                    print(popupMessageTitle)
                    popupTextMessage = struct.unpack_from('!4s', data, offset)[0]
                    print(popupTextMessage)
                elif ord(robotMessageType) == 7:
                    robotMessageCode = self.__unpack(data, DataFormat.INT, SizeFormat.INT)
                    robotMessageArgument = self.__unpack(data, DataFormat.INT, SizeFormat.INT)
                    robotMessageTitleSize = self.__unpack(data, DataFormat.UNSIGNED_CHAR, SizeFormat.UNSIGNED_CHAR)
                    robotMessageTitle = struct.unpack_from('!%ds' % robotMessageTitleSize, data, offset)[0]
                    print(robotMessageTitle)
                    keyTextMessage = struct.unpack_from('!8s', data, offset)[0]
                    print(keyTextMessage)
