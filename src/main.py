from abc import ABC, abstractmethod
from f3 import F3
import numpy as np

# 命令の抽象クラス
class MyInterface(ABC):
    @abstractmethod
    def getParameterSize(self):
        pass

    @abstractmethod
    def execute(self, parameter):
        pass

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
        print("c3 executed.")
        print(parameter)


# 命令クラステーブル
instruction_class_table = {
    "f3": F3,
    "c3": C3
}

# フラグレジスタ
class FlagRegister:
    def __init__(self,Register_Z):
        self.Register_Z = Register_Z

# レジスタ
Reg_A = 0
Reg_B = 0
Reg_C = 0
Reg_D = 0
Reg_E = 0
Reg_F = 0
Reg_H = 0
Reg_L = 0
pc = 0
sp = 0
Reg_Flag = FlagRegister(0)

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
            print(instruction_code.hex())
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

