from enum import Enum


class ControlModes(Enum):
    CONTROL_MODE_POSITION = 0
    CONTROL_MODE_TEACH = 1
    CONTROL_MODE_FORCE = 2
    CONTROL_MODE_TORQUE = 3


class RobotModes(Enum):
    ROBOT_MODE_NO_CONTROLLER = -1
    ROBOT_MODE_DISCONNECTED = 0
    ROBOT_MODE_CONFIRM_SAFETY = 1
    ROBOT_MODE_BOOTING = 2
    ROBOT_MODE_POWER_OFF = 3
    ROBOT_MODE_POWER_ON = 4
    ROBOT_MODE_IDLE = 5
    ROBOT_MODE_BACKDRIVE = 6
    ROBOT_MODE_RUNNING = 7
    ROBOT_MODE_UPDATING_FIRMWARE = 8


class JointModes(Enum):
    JOINT_MODE_RESET = 235
    JOINT_MODE_SHUTTING_DOWN = 236
    JOINT_MODE_BACKDRIVE = 238
    JOINT_MODE_POWER_OFF = 239
    JOINT_MODE_READY_FOR_POWER_OFF = 240
    JOINT_MODE_NOT_RESPONDING = 245
    JOINT_MODE_MOTOR_INITIALISATION = 246
    JOINT_MODE_BOOTING = 247
    JOINT_MODE_VIOLATION = 251
    JOINT_MODE_FAULT = 252
    JOINT_MODE_RUNNING = 253
    JOINT_MODE_IDLE = 255


class ToolModes(Enum):
    JOINT_MODE_RESET = 235
    JOINT_MODE_SHUTTING_DOWN = 236
    JOINT_MODE_POWER_OFF = 239
    JOINT_MODE_NOT_RESPONDING = 245
    JOINT_MODE_BOOTING = 247
    JOINT_MODE_BOOTLOADER = 249
    JOINT_MODE_FAULT = 252
    JOINT_MODE_RUNNING = 253
    JOINT_MODE_IDLE = 255


class MessageSource(Enum):
    MESSAGE_SOURCE_JOINT_0_FPGA = 100
    MESSAGE_SOURCE_JOINT_0_A = 110
    MESSAGE_SOURCE_JOINT_0_B = 120
    MESSAGE_SOURCE_JOINT_1_FPGA = 101
    MESSAGE_SOURCE_JOINT_1_A = 111
    MESSAGE_SOURCE_JOINT_1_B = 121
    MESSAGE_SOURCE_JOINT_2_FPGA = 102
    MESSAGE_SOURCE_JOINT_2_A = 112
    MESSAGE_SOURCE_JOINT_2_B = 122
    MESSAGE_SOURCE_JOINT_3_FPGA = 103
    MESSAGE_SOURCE_JOINT_3_A = 113
    MESSAGE_SOURCE_JOINT_3_B = 123
    MESSAGE_SOURCE_JOINT_4_FPGA = 104
    MESSAGE_SOURCE_JOINT_4_A = 114
    MESSAGE_SOURCE_JOINT_4_B = 124
    MESSAGE_SOURCE_JOINT_5_FPGA = 105
    MESSAGE_SOURCE_JOINT_5_A = 115
    MESSAGE_SOURCE_JOINT_5_B = 125
    MESSAGE_SOURCE_TOOL_FPGA = 106
    MESSAGE_SOURCE_TOOL_A = 116
    MESSAGE_SOURCE_TOOL_B = 126
    MESSAGE_SOURCE_EUROMAP_FPGA = 107
    MESSAGE_SOURCE_EUROMAP_A = 117
    MESSAGE_SOURCE_EUROMAP_B = 127
    MESSAGE_SOURCE_TEACH_PENDANT_A = 108
    MESSAGE_SOURCE_TEACH_PENDANT_B = 118
    MESSAGE_SOURCE_SCB_FPGA = 40
    MESSAGE_SAFETY_PROCESSOR_UA = 20
    MESSAGE_SAFETY_PROCESSOR_UB = 30
    MESSAGE_SOURCE_ROBOTINTERFACE = -2
    MESSAGE_SOURCE_RTMACHINE = -3
    MESSAGE_SOURCE_SIMULATED_ROBOT = -4
    MESSAGE_SOURCE_GUI = -5
    MESSAGE_SOURCE_CONTROLLER = 7
    MESSAGE_SOURCE_RTDE = 8


class MessageType(Enum):
    MESSAGE_TYPE_DISCONNECT = -1
    MESSAGE_TYPE_ROBOT_STATE = 16
    MESSAGE_TYPE_ROBOT_MESSAGE = 20
    MESSAGE_TYPE_HMC_MESSAGE = 22
    MESSAGE_TYPE_MODBUS_INFO_MESSAGE = 5
    MESSAGE_TYPE_SAFETY_SETUP_BROADCAST_MESSAGE = 23
    MESSAGE_TYPE_SAFETY_COMPLIANCE_TOLERANCES_MESSAGE = 24
    MESSAGE_TYPE_PROGRAM_STATE_MESSAGE = 25


class SafetyMode(Enum):
    SAFETY_MODE_UNDEFINED_SAFETY_MODE = 11
    SAFETY_MODE_VALIDATE_JOINT_ID = 10
    SAFETY_MODE_FAULT = 9
    SAFETY_MODE_VIOLATION = 8
    SAFETY_MODE_ROBOT_EMERGENCY_STOP = 7
    SAFETY_MODE_SYSTEM_EMERGENCY_STOP = 6
    SAFETY_MODE_SAFEGUARD_STOP = 5
    SAFETY_MODE_RECOVERY = 4
    SAFETY_MODE_PROTECTIVE_STOP = 3
    SAFETY_MODE_REDUCED = 2
    SAFETY_MODE_NORMAL = 1


class SafetyStatus(Enum):
    SAFETY_STATUS_SYSTEM_THREE_POSITION_ENABLING_STOP = 13
    SAFETY_STATUS_AUTOMATIC_MODE_SAFEGUARD_STOP = 12
    SAFETY_STATUS_UNDEFINED_SAFETY_MODE = 11
    SAFETY_STATUS_VALIDATE_JOINT_ID = 10
    SAFETY_STATUS_FAULT = 9
    SAFETY_STATUS_VIOLATION = 8
    SAFETY_STATUS_ROBOT_EMERGENCY_STOP = 7
    SAFETY_STATUS_SYSTEM_EMERGENCY_STOP = 6
    SAFETY_STATUS_SAFEGUARD_STOP = 5
    SAFETY_STATUS_RECOVERY = 4
    SAFETY_STATUS_PROTECTIVE_STOP = 3
    SAFETY_STATUS_REDUCED = 2
    SAFETY_STATUS_NORMAL = 1


class ReportLevel(Enum):
    REPORT_LEVEL_DEBUG = 0  # INTERNAL USE ONLY
    REPORT_LEVEL_INFO = 1
    REPORT_LEVEL_WARNING = 2
    REPORT_LEVEL_VIOLATION = 3
    REPORT_LEVEL_FAULT = 4
    REPORT_LEVEL_DEVL_DEBUG = 128  # INTERNAL USE ONLY
    REPORT_LEVEL_DEVL_INFO = 129
    REPORT_LEVEL_DEVL_WARNING = 130
    REPORT_LEVEL_DEVL_VIOLATION = 131
    REPORT_LEVEL_DEVL_FAULT = 132


class RequestValue(Enum):
    REQUEST_VALUE_TYPE_BOOLEAN = 0
    REQUEST_VALUE_TYPE_INTEGER = 1
    REQUEST_VALUE_TYPE_FLOAT = 2
    REQUEST_VALUE_TYPE_STRING = 3
    REQUEST_VALUE_TYPE_POSE = 4
    REQUEST_VALUE_TYPE_JOINTVECTOR = 5
    REQUEST_VALUE_TYPE_WAYPOINT = 6  # UNUSED
    REQUEST_VALUE_TYPE_EXPRESSION = 7  # UNUSED
    REQUEST_VALUE_TYPE_NONE = 8


class DataFormat(Enum):
    """
    Based on https://docs.python.org/3/library/struct.html
    """
    CHAR = 'c'
    SIGNED_CHAR = 'b'
    UNSIGNED_CHAR = 'B'
    BOOLEAN = '?'
    SHORT = 'h'
    UNSIGNED_SHORT = 'H'
    INT = 'i'
    UNSIGNED_INT = 'I'
    LONG = 'l'
    UNSIGNED_LONG = 'L'
    LONG_LONG = 'q'
    UNSIGNED_LONG_LONG = 'Q'
    FLOAT = 'f'
    DOUBLE = 'd'
    STRING = 's'


class SizeFormat(Enum):
    CHAR = 1
    SIGNED_CHAR = 1
    UNSIGNED_CHAR = 1
    BOOLEAN = 1
    SHORT = 2
    UNSIGNED_SHORT = 2
    INT = 4
    UNSIGNED_INT = 4
    LONG = 4
    UNSIGNED_LONG = 4
    LONG_LONG = 8
    UNSIGNED_LONG_LONG = 8
    FLOAT = 4
    DOUBLE = 8