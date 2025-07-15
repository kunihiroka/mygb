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
        self.sp = int('FFFE',16)
        self.pc = 0
        self.z = 0
        self.n = 0
        self.h = 0
        self.c = 0
    
    def SetA(self,value):
        self.a = value & 0xFF    # 1byteでマスク

    def GetA(self):
        return self.a

    def SetB(self,value):
        self.b= value & 0xFF    # 1byteでマスク

    def GetB(self):
        return self.b

    def SetC(self,value):
        self.c= value & 0xFF    # 1byteでマスク

    def GetC(self):
        return self.c

    def SetD(self,value):
        self.d= value & 0xFF    # 1byteでマスク

    def GetD(self):
        return self.d

    def SetE(self,value):
        self.e= value & 0xFF    # 1byteでマスク

    def GetE(self):
        return self.e

    def SetF(self,value):
        self.f= value & 0xFF    # 1byteでマスク

    def GetF(self):
        return self.f

    def SetH(self,value):
        self.h= value & 0xFF    # 1byteでマスク

    def GetH(self):
        return self.h

    def SetL(self,value):
        self.l= value & 0xFF    # 1byteでマスク

    def GetL(self):
        return self.l

    def SetHL(self, value):
        self.h = (value >> 8) & 0xFF
        self.l = value & 0xFF

    def GetHL(self):
        return (self.h << 8) | self.l
    
    def SetAF(self, value):
        self.a = (value >> 8) & 0xFF
        self.f = value & 0xFF
    
    def GetAF(self):
        return (self.a << 8) | self.f
    
    def SetBC(self, value):
        self.b = (value >> 8) & 0xFF
        self.c = value & 0xFF
    
    def GetBC(self):
        return (self.b << 8) | self.c

    def SetDE(self, value):
        self.d = (value >> 8) & 0xFF
        self.e = value & 0xFF
    
    def GetDE(self):
        return (self.d << 8) | self.e

    def SetSP(self,value):
        self.sp= value & 0xFFFF    # 2byteでマスク

    def GetSP(self):
        return self.sp

    def SetPC(self,value):
        self.pc= value & 0xFFFF    # 2byteでマスク

    def GetPC(self):
        return self.pc

    def SetZ(self,value):
        self.z = value & 0x1    # 1bitでマスク

    def GetZ(self):
        return self.z

    def SetN(self,value):
        self.n = value & 0x1    # 1bitでマスク

    def GetN(self):
        return self.n



