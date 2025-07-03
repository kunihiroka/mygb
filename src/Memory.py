MEMORY_SIZE = 65535

# 0000-7FFF ROM
# 8000-BFFF 8kb Video RAM
# C000-DFFF 8kb Internal RAM
# E000-FDFF Echo of 8kb internal RAM
# FE00-FEBF Sprite Attrib Memory (0AM)
# FEA0-FEFF Empty but unsusabel for I/O
# FF00-FE4D I/O ports
# FE4C-FF7F Empty but unusable for I/O
# FF80-FFFF Internal RAM

class Memory:
    def __init__(self):
        self.memory = [b'\x00'] * MEMORY_SIZE

    def LoadRom(self, rom_path):
        with open(rom_path, 'rb') as file:
            file.seek(0, 2)                 # ファイルの末尾に移動(2は末尾からの相対位置)
            rom_size = file.tell()      # 現在位置(=ファイルサイズ)
            file.seek(0)                    # 先頭に移動
            
            count = 0
            while count < rom_size:
                self.memory[count] = file.read(1)       # 1byte 読み出し
                # file.seek(1, 1)                       # 読み出し位置を進める
                                                        # file.readだけで自動的にポインタは1進むので、seekは不要。
                count += 1


