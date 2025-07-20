from InstructionInterface import MyInterface

# OR命令
# Logical OR n with register A. result in A.

class OR(MyInterface):
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        if opcode == 0xb1:
            parameter_size = 0
        else:
            print("undefined opcode")
            parameter_size = 0

        return parameter_size

    def execute(self, opcode, parameter, register, memory):
        print("paraemter:", parameter)

        if opcode == 0xb1:
            """
            A or C
            """
            temp = register.GetA() | register.GetC()
            register.SetA(temp)

            if temp == 0:
                register.SetZ(1)
            else:
                register.SetZ(0)
            
            register.SetN(0)
            register.SetH(0)
            register.SetC(0)

            print("b1 executed.")
            clock = 4
        else:
            print("error.")
            clock = 0

        return clock
