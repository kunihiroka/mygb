from InstructionInterface import MyInterface

# LDH命令
class LDH(MyInterface):
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        if opcode == 0xe0:
            parameter_size = 1
        elif opcode == 0xf0:
            parameter_size = 1
        else:
            print("undefined opcode")
            parameter_size = 0

        return parameter_size

    def execute(self, opcode, parameter, register, memory):
        print("paraemter:", parameter)

        if opcode == 0xe0:
            """
            Paramter = ($FF00+n),A
            """
            address = 0xff00 + parameter
            memory.SetMemory(address, register.GetA())
            print("e0 executed.")
            clock = 12
        elif opcode == 0xf0:
            """
            Put memory address $FF00+n into A
            FF00-FF8F     I/O Ports
            """
            address = 0xff00 + parameter
            register.SetA(memory.GetMemory(address))
            print("f0 executed.")
            clock = 12
        else:
            print("error.")
            clock = 0

        return clock
