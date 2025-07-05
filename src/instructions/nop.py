from InstructionInterface import MyInterface

# NOP命令
class NOP(MyInterface):
    """
    NOP
    No operation
    """
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        return 0

    def execute(self, opcode, parameter, register, memory):
        print("00 executed.")

