from InstructionInterface import MyInterface

# F3命令
class F3(MyInterface):
    """
    DI:
    This instruction disables interrupts but not immediately.
    Interrupts are disabled after instruction DI is executed.
    """
    def __init__(self, name):
        self.name = name

    def getParameterSize(self):
        return 0

    def execute(self, parameter):
        print("f3 executed.")
        print("parameter:", parameter)

