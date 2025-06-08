class Register:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.f = 0
        self.h = 0
        self.l = 0
        self.sp = 0
        self.pc = 0
        self.z = 0
        self.n = 0
        self.h = 0
        self.c = 0
    
    def SetA(value):
        self.a = value & 0xF    # 1byteでマスク

    def GetA():
        return self.a

    def SetB(value):
        self.b= value & 0xF    # 1byteでマスク

    def GetB():
        return self.b

    def SetC(value):
        self.c= value & 0xF    # 1byteでマスク

    def GetC():
        return self.c
