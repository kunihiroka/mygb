# LCD Controller

class LCDC:
    def __init__(self):
        pass

    def scan(sefl, register, memory):
        ly = memory.GetMemory(0xff44)
        memory.SetMemory(0xff44,ly + 1)
