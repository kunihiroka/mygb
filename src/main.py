from Register import Register
from Memory import Memory
from lcdc import LCDC
from instructions.di import DI
from instructions.jp import JP
from instructions.add import ADD
from instructions.ld import LD
from instructions.call import CALL
from instructions.nop import NOP
from instructions.ldh import LDH
from instructions.cp import CP
from instructions.jr import JR
import numpy as np

reg = Register()
mem = Memory()
lcdc = LCDC()

# 命令クラステーブル
instruction_class_table = {
    "00": NOP,
    "38": JR,
    "66": LD,
    "c3": JP,
    "cc": CALL,
    "ce": ADD,
    "f0": LDH,
    "f3": DI,
    "fe": CP,
}

# 命令インスタンス取得
def get_instruction_object(instruction_name):
    instruction_class = instruction_class_table.get(instruction_name)

    if instruction_class:
        return instruction_class("inst")
    else:
        raise ValueError("unknown class")


def main():
    # クロック変数
    clock = 0

    # レジスタ定義
    pc = np.uint16(0)

    # 読み出すROMのパスを設定
    rom_path = './rom/hello-world.gb'

    # ROMファイルの読み込み(Memoryクラス)
    mem = Memory()
    mem.LoadRom(rom_path)

    # ROMファイルの読み込み
    with open(rom_path, 'rb') as file: # 'rb'で開くとバイナリ読み込みになる。
        reg.SetPC(int('100', 16))

        while True:                             # とりま無限ループ。
            # --- CPU ---
            if clock == 0:                      # clockカウンタが0(CPU空き)の場合
                # 次の命令実行
                file.seek(reg.GetPC())

                # 命令コード読み出し
                instruction_code = file.read(1)          # 1byte読み出し
                reg.SetPC(reg.GetPC() + 1)

                # 命令オブジェクトの取得
                print("instruction code:", instruction_code.hex())
                instruction_object = get_instruction_object(instruction_code.hex())

                # パラメータ読み出し
                ## その命令のパラメータサイズを取得
                parameter_size = instruction_object.getParameterSize(instruction_code.hex())
                ## パラメータ読み出し
                parameter = file.read(parameter_size)
                reg.SetPC(reg.GetPC() + parameter_size)

                # 命令実行
                clock = instruction_object.execute(instruction_code.hex(), parameter, reg, mem)
            
            # クロック消費
            if clock > 0:
                clock -= 1

            # --- ペリフェラル ---
            ## LCDC
            lcdc.scan(reg, mem)

if __name__ == '__main__':
    main()

