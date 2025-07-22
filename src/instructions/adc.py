from InstructionInterface import MyInterface

class ADC(MyInterface):
    """
    ADC A,n
    Add n + Carry flag to A
    """
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        if opcode == 0x88:
            parameter_size = 0
        else
            print("undefined opcode")
            parameter_size = 0

        return parameter_size

    def execute(self, opcode, parameter, register, memory):
        if opcode == 0x88:
            # ADC A, B
            register.SetA(register.GetB() = register.GetC())
            print("88 executed.")
            clock = 4
        else:
            print("undefined opcode")
            clock = 0

        return clock

