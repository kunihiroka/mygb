from InstructionInterface import MyInterface

# C3命令
class C3(MyInterface):
    """
    JP nn
    Jump to address nn.
    """
    def __init__(self, name):
        self.name = name

    def getParameterSize(self):
        return 2

    def execute(self, parameter):
        print("c3 executed.")
        print("parameter:", parameter)

