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
        if opcode == 0x01:
            # LD BC, nn
            parameter_size = 2
        elif opcode == 0x11:
            # LD DE, nn
            parameter_size = 2
        elif opcode == 0x21:
            # LD HL, nn
            parameter_size = 2
        elif opcode == 0x44:
            # LD B,H
            parameter_size = 0
        elif opcode == 0x66:
            # LD H,(HL)
            parameter_size = 0
        elif opcode == 0x68:
            parameter_size = 0
        else:
            print("undefined opcode")
            parameter_size = 0

        return parameter_size

    def execute(self, opcode, parameter, register, memory):
        print("paraemter:", parameter)

        if opcode == 0x01:
            # LD BC,nn
            register.SetBC(parameter)
            clock = 12
        elif opcode == 0x11:
            # LD DE,nn
            register.SetDE(parameter)
            clock = 12
        elif opcode == 0x21:
            # LD HL,nn
            register.SetHL(parameter)
            clock = 12
        elif opcode == 0x44:
            # LD B,H
            register.SetB(register.GetH())
            print("44 executed.")
            clock = 4
        elif opcode == 0x66:
            # LD H,(HL)
            temp1 = register.GetH()
            temp2 = temp1 + memory.GetMemory(register.GetHL())
            register.SetH(temp2)
            print("66 executed.")
            clock = 8
        elif opcode == 0x68:
            # LD L,B
            register.SetL(register.GetB())
            print("68 executed.")
            clock = 4
        else:
            print("error.")
            clock = 0

        return clock
