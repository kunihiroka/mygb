# LCD Controller

class LCDC:
    def __init__(self):
        pass

    def scan(sefl, register, memory):
        ly = memory.GetMemory(0xff44)
        ly += 1

        # The values between 144 and 153 indicate the V-Blank period.
        if ly > 153:
            ly = 0

        memory.SetMemory(0xff44,ly)
