from InstructionInterface import MyInterface

# LDI命令
# Put A into memory address HL. Increment HL.
# Same as: LD (HL), A - INC HL
class LDI(MyInterface):
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        if opcode == 0x22:
            parameter_size = 0
        else:
            print("undefined opcode")
            parameter_size = 0

        return parameter_size

    def execute(self, opcode, parameter, register, memory):
        print("paraemter:", parameter)

        if opcode == 0x22:
            memory.SetMemory(register.GetHL(), register.GetA())
            register.SetHL(register.GetHL() + 1)
            print("22 executed.")
            clock = 12
        else:
            print("error.")
            clock = 0

        return clock
