from InstructionInterface import MyInterface

# DEC命令
# Decrement register n.

class DEC(MyInterface):
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        if opcode == 0x0d:
            parameter_size = 0
        else:
            print("undefined opcode")
            parameter_size = 0

        return parameter_size

    def execute(self, opcode, parameter, register, memory):
        print("paraemter:", parameter)

        if opcode == 0x0d:
            """
            Decrement C
            """
            temp = register.GetC() - 1
            register.SetC(temp)

            if temp == 0:
                register.SetZ(1)
            else:
                register.SetZ(0)
            
            register.SetN(1)

            if ((0x0F & register.GetC()) < (0x0F & 1)):
                register.SetH(1)
            else:
                register.SetH(0)
            

            print("0d executed.")
            clock = 4
        else:
            print("error.")
            clock = 0

        return clock
