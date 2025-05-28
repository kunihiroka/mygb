from abc import ABC, abstractmethod
import mygb

import numpy as np

# 命令の抽象クラス
class MyInterface(ABC):
    @abstractmethod
    def getParameterSize(self):
        pass

    @abstractmethod
    def execute(self, parameter):
        pass

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
        print("f3 implemented as class")
        print(parameter)

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
        print("c3 implemented as class")
        print(parameter)


# 命令クラステーブル
instruction_class_table = {
    "f3": F3,
    "c3": C3
}

# 命令インスタンス取得
def get_instruction_object(instruction_name):
    instruction_class = instruction_class_table.get(instruction_name)

    if instruction_class:
        return instruction_class("inst")
    else:
        raise ValueError("unknown class")



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
            instruction_code = file.read(1)          # 1byte読み出し
            pc = pc + 1

            # 命令オブジェクトの取得
            instruction_object = get_instruction_object(instruction_code.hex())

            # パラメータ読み出し
            ## その命令のパラメータサイズを取得
            parameter_size = instruction_object.getParameterSize()
            ## パラメータ読み出し
            parameter = file.read(parameter_size)
            pc = pc + parameter_size

            # 命令実行
            instruction_object.execute(parameter)


if __name__ == '__main__':
    main()

