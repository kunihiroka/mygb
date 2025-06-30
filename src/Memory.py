MEMORY_SIZE = 65535

class Memory:
    def __init__(self):
        self.memory = bytearray(MEMORY_SIZE)

    def LoadRom(self, rom_path):
        with open(rom_path, 'rb') as file:
            file.seek(0, 2)                 # ファイルの末尾に移動(2は末尾からの相対位置)
            rom_size = file.tell()      # 現在位置(=ファイルサイズ)
            file.seek(0)                    # 先頭に移動
            
            count = 0
            while count < rom_size:
                self.memory[count] = file.read(1)       # 1byte 読み出し
                file.seek(1, 1)                         # 読み出し位置を進める

                count += 1
