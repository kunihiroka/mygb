from InstructionInterface import MyInterface

class JP(MyInterface):
    """
    JP nn
    Jump to address nn.
    """
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        return 2

    def execute(self, opcode, parameter, register, memory):
        register.SetPC(int(parameter.hex(),16))
        print("c3 executed.")
        print("parameter:", parameter)
        clock = 12

        return clock
