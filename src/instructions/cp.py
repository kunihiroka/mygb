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

        if opcode == "f0":
            print("fe executed.")
        else:
            print("error.")

