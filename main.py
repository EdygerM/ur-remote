from ur_remote.URRobot import URRobot

if __name__ == '__main__':
    robotSFC = URRobot("192.168.0.21")
    robotNMR = URRobot("192.168.0.22")
    robotSFC.runProgram("pickSFCCircuit")
    robotSFC.runProgram("putSFCStock")
    robotSFC.runProgram("pickRMNStock")
    robotSFC.runProgram("putRMNSJ")
    robotSFC.runProgram("pickRMNSJ")
    robotSFC.runProgram("putRMNStock")
    robotSFC.runProgram("pickSFCStock")
    robotSFC.runProgram("putSFCCircuit")



