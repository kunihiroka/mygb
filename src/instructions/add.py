from InstructionInterface import MyInterface

class ADD(MyInterface):
    """
    ADD A,n
    Add n + Carry Flag to A.
    """
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        return 1

    def execute(self, opcode, parameter, register, memory):
        print("ce executed.")
        print("paraemter:", parameter)

        register.SetA(register.GetA() + parameter)
        clock = 8

        return clock

