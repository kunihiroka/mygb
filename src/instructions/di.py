from InstructionInterface import MyInterface

class DI(MyInterface):
    """
    DI:
    This instruction disables interrupts but not immediately.
    Interrupts are disabled after instruction DI is executed.
    """
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        return 0

    def execute(self, opcode, parameter, register, memory):
        print("f3 executed.")
        print("parameter:", parameter)
        
        return 0
