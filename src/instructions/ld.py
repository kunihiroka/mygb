from InstructionInterface import MyInterface

# LD命令
class LD(MyInterface):
    """
    LD r1,r2
    Put value r2 into r1.
    r1,r2 = A,B,C,D,E,H,L,(HL)
    """
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        if opcode == "66":
            # LD H,(HL)
            parameter_size = 0
        else:
            print("undefined opcode")
            parameter_size = 0

        return parameter_size

    def execute(self, opcode, parameter, register, memory):
        print("paraemter:", parameter)

        if opcode == "66":
            # LD H,(HL)
            temp1 = register.GetH()
            temp2 = temp1 + memory.GetMemory(register.GetHL())
            register.SetH(temp2)
            print("66 executed.")
            clock = 8
        else:
            print("error.")
            clock = 0

        return clock
