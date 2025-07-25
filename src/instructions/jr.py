from InstructionInterface import MyInterface

# JR命令
class JR(MyInterface):
    """
    if following condition is true, then add n to current address and jump to it
    """
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        if opcode == 0x20:
            # JR NZ
            parameter_size = 1
        elif opcode == 0x38:
            # JR C,*
            parameter_size = 1
        else:
            print("undefined opcode")
            parameter_size = 0

        return parameter_size

    def execute(self, opcode, parameter, register, memory):
        print("paraemter:", parameter)

        if opcode == 0x20:
            # JR NZ,*
            if register.GetZ() == 0:
                register.SetPC(register.GetPC() + parameter)

            print("20 executed")
            clock = 8
        elif opcode == 0x38:
            # JR C,*
            if register.GetC() == 1:
                register.SetPC(register.GetPC() + parameter)

            print("38 executed.")
            clock = 8
        else:
            print("error.")
            clock = 0

        return clock

