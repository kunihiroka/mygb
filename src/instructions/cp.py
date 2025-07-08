from InstructionInterface import MyInterface

class CP(MyInterface):
    """
    CP:
    Compare A with n. This is basically an A - n subtraction instruction but the results are thrown away.
    """
    def __init__(self, name):
        self.name = name

    def getParameterSize(self, opcode):
        if opcode == "fe":
            parameter_size = 1
        else:
            print("undefined opcode")
            parameter_size = 0

        return parameter_size

    def execute(self, opcode, parameter, register, memory):
        print("parameter:", parameter)

        if opcode == "fe":
            # ゼロフラグ、キャリーフラグ
            temp = register.GetA() - parameter
            if temp == 0:
                register.SetZ(1)
            elif temp < 0:
                register.SetC(1)
            else: # temp < 0

            # ハーフキャリアフラグ
            if ((0x0F & register.GetA()) < (0x0F & parameter)):
                register.SetH(1)
            
            # Subtractフラグ
            register.SetN(1)

            print("fe executed.")
        else:
            print("error.")

