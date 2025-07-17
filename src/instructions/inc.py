from InstructionInterface import MyInterface

class INC(MyInterface):
    """
    INC
    increment register nn.
    """
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        if opcode == 0x13:
            # INC DE
            parameter_size = 0
        else:
            print("undefined opcode")
            parameter_size = 0

        return 2

    def execute(self, opcode, parameter, register, memory):
        if opcode == 0x13:
            register.SetDE(register.GetDE() + 1)
            print("13 executed.")
            clock = 8
        else:
            print("error.")
            clock = 0

        return clock
