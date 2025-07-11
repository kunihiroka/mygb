from InstructionInterface import MyInterface

# LDH命令
class LDH(MyInterface):
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        if opcode == "f0":
            parameter_size = 1
        else:
            print("undefined opcode")
            parameter_size = 0

        return parameter_size

    def execute(self, opcode, parameter, register, memory):
        print("paraemter:", parameter)

        if opcode == "f0":
            """
            Put memory address $FF00+n into A
            FF00-FF8F     I/O Ports
            """
            address = 0xff00 + int(parameter.hex(),16)
            register.SetA(int(memory.GetMemory(address).hex(),16))
            print("f0 executed.")
            clock = 12
        else:
            print("error.")
            clock = 0

        return clock
