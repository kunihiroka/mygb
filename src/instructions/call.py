from InstructionInterface import MyInterface

# CALL命令
class CALL(MyInterface):
    """
    CALL cc,nn
    Call address n if following condition is true:
        cc = NZ,    Call if Z flag is reset.
        cc = Z,     Call if Z flag is set.
        cc = NC,    Call if C flag is reset.
        cc = C,     Call if C flag is set.
    """
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        if opcode == 0xcc:
            # CALL Z, nn
            parameter_size = 2
        else:
            print("undefined opcode")
            parameter_size = 0

        return parameter_size

    def execute(self, opcode, parameter, register, memory):
        print("paraemter:", parameter.hex())
        if opcode == 0xcc:
            # CALL Z, nn
            register.SetSP(register.GetSP() - 1)
            memory.SetMemory(register.GetSP(), register.GetPC() + 1)
            register.SetPC(parameter)
            print("PC",register.GetPC())
            print("cc executed.")
            clock = 12
        else:
            print("undefined opcode")
            clock = 0

        return clock

