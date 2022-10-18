import socket, struct

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

    def connect(self):
        """
        Connect to the Universal Robot primary Server

        :return: The status of the connection
        :rtype: string
        """

        self.server.connect((self.ipAddress, PRIMARY_PORT))

        return self.server.recv(1024)

    def readPort(self):
        """

        """
        data = self.server.recv(4096)
        offset = 0
        if data:
            messageSize = struct.unpack_from('!i', data)[0]
            offset += 4
            messageType = struct.unpack_from('!B', data, offset)[0]
            offset += 1
            if messageType == 20:
                timestamp = struct.unpack_from('!Q', data, offset)[0]
                offset += 8
                source = struct.unpack_from('!c', data, offset)[0]
                offset += 1
                robotMessageType = struct.unpack_from('!c', data, offset)[0]
                offset += 1
                print(ord(robotMessageType))
                if ord(robotMessageType) == 9:
                    requestId = struct.unpack_from('!I', data, offset)[0]
                    offset += 4
                    requestedType = struct.unpack_from('!I', data, offset)[0]
                    offset += 4
                    warning = struct.unpack_from('!?', data, offset)[0]
                    offset += 1
                    error = struct.unpack_from('!?', data, offset)[0]
                    offset += 1
                    blocking = struct.unpack_from('!?', data, offset)[0]
                    offset += 1
                    popupMessageTitleSize = struct.unpack_from('!B', data, offset)[0]
                    offset += 1
                    popupMessageTitle = struct.unpack_from('!%ds' % popupMessageTitleSize, data, offset)[0]
                    offset += popupMessageTitleSize
                    print(popupMessageTitle)
                    popupTextMessage = struct.unpack_from('!4s', data, offset)[0]
                    print(popupTextMessage)
                elif ord(robotMessageType) == 7:
                    robotMessageCode = struct.unpack_from('!i', data, offset)[0]
                    offset += 4
                    robotMessageArgument = struct.unpack_from('!i', data, offset)[0]
                    offset += 4
                    robotMessageTitleSize = struct.unpack_from('!B', data, offset)[0]
                    offset += 1
                    robotMessageTitle = struct.unpack_from('!%ds' % robotMessageTitleSize, data, offset)[0]
                    offset += robotMessageTitleSize
                    print(robotMessageTitle)
                    keyTextMessage = struct.unpack_from('!8s', data, offset)[0]
                    print(keyTextMessage)









