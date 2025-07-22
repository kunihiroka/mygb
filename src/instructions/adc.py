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
            temp = register.GetB() + register.GetCFlag()
            register.SetA(temp)

            # Z Flag
            if temp == 0:
                register.SetZFlag(1)
            else:
                register.SetZFlag(0)

            # N Flag
            register.SetNFlag(0)

            # H Flag
            if ((register.GetB() & 0x0F + register.GetCFlag() & 0x0F) > 15):
                register.SetHFlag(1)
            else:
                register.SetHFlag(0)

            # C Flag
            if ((register.GetB() + register.GetCFlag()) > 255):
                register.SetCFlag(1)
            else:
                register.SetCFlag(0)

            print("88 executed.")
            clock = 4
        else:
            print("undefined opcode")
            clock = 0

        return clock

