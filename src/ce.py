from InstructionInterface import MyInterface

# CE命令
class CE(MyInterface):
    """
    ADD A,n
    Add n + Carry Flag to A.
    """
    def __init__(self, name):
        self.name = name

    def getParameterSize(self):
        return 1

    def execute(self, parameter):
        print("ce executed.")
        print("paraemter:",parameter)
