from abc import ABC, abstractmethod
import mygb

import numpy as np

class MyInterface(ABC):
    @abstractmethod
    def getParameterSize(self):
        pass

    @abstractmethod
    def execute(self, parameter):
        pass

class F3(MyInterface):
    def getParameterSize(self):
        return 0

    def execute(self, parameter):
        print("f3 implemented as class")

class GbInstructions:
    F3_PRM_SIZE = 0
    def f3(prm):
        """
        DI:
        This instruction disables interrupts but not immediately.
        Interrupts are disabled after instruction DI is executed.
        """
        print('f3')
        print(prm)

    C3_PRM_SIZE = 2
    def c3(prm):
        """
        JP nn
        Jump to address nn.
        """
        print('c3')
        print(prm)

parameter_size_table = {
    "f3": GbInstructions.F3_PRM_SIZE,
    "c3": GbInstructions.C3_PRM_SIZE,
}

instruction_table = {
    "f3": GbInstructions.f3,
    "c3": GbInstructions.c3,
}

def main():
    # レジスタ定義
    pc = np.uint16(0)

    # 読み出すROMのパスを設定
    rom_path = './rom/hello-world.gb'

    # ROMファイルの読み込み
    with open(rom_path, 'rb') as file: # 'rb'で開くとバイナリ読み込みになる。
        pc = int('100', 16)

        while True:                             # とりま無限ループ。
            file.seek(pc)

            # 命令コード読み出し
            data = file.read(1)          # 1byte読み出し
            pc = pc + 1

            # パラメータ読み出し
            prm_size = parameter_size_table[data.hex()]
            prm = file.read(prm_size)
            pc = pc + prm_size

            # 命令実行
            instruction_table[data.hex()](prm)


if __name__ == '__main__':
    main()

