from InstructionInterface import MyInterface

# XOR命令
# Logical exclusive OR n with register A, result in A.
class XOR(MyInterface):
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        if opcode == 0xaf:
            parameter_size = 0
        else:
            print("undefined opcode")
            parameter_size = 0

        return parameter_size

    def execute(self, opcode, parameter, register, memory):
        print("paraemter:", parameter)

        if opcode == 0xaf:
            """
            A xor A
            """
            register.SetA(register.GetA() ^ register.GetA())
            print("af executed.")
            clock = 4
        else:
            print("error.")
            clock = 0

        return clock
