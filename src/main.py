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
from instructions.xor import XOR
import numpy as np

reg = Register()
mem = Memory()
lcdc = LCDC()

# 命令クラステーブル
instruction_class_table = {
    "00": NOP,
    "01": LD,
    "11": LD,
    "21": LD,
    "38": JR,
    "44": LD,
    "66": LD,
    "68": LD,
    "af": XOR,
    "c3": JP,
    "cc": CALL,
    "ce": ADD,
    "e0": LDH,
    "f0": LDH,
    "f3": DI,
    "fe": CP,
}

# 命令インスタンス取得
def get_instruction_object(instruction_name):
    instruction_class = instruction_class_table.get(format(instruction_name, 'x'))

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
        reg.SetPC(0x100)

        while True:                             # とりま無限ループ。
            # --- CPU ---
            if clock == 0:                      # clockカウンタが0(CPU空き)の場合
                # 次の命令実行
                # file.seek(reg.GetPC())

                # 命令コード読み出し
                instruction_code = mem.GetMemory(reg.GetPC())
                # instruction_code = file.read(1)          # 1byte読み出し
                reg.SetPC(reg.GetPC() + 1)

                # 命令オブジェクトの取得
                print("instruction code:", format(instruction_code, 'x'))
                instruction_object = get_instruction_object(instruction_code)

                # パラメータ読み出し
                ## その命令のパラメータサイズを取得
                parameter_size = instruction_object.getParameterSize(instruction_code)
                ## パラメータ読み出し
                parameter = 0x00
                shift = 0
                while parameter_size > 0:
                    parameter = parameter << (shift*8)              # シフトして読み出し先を空ける
                    parameter |= mem.GetMemory(reg.GetPC())         # パラメータ読み出し
                    reg.SetPC(reg.GetPC() + 1)                      # プログラムカウンタ更新
                    parameter_size -= 1                             # ループカウンタデクリメント
                    shift += 1                                      # シフトサイズカウンタデクリメント
                # parameter = file.read(parameter_size)
                # reg.SetPC(reg.GetPC() + parameter_size)

                # 命令実行
                clock = instruction_object.execute(instruction_code, parameter, reg, mem)
            
            # クロック消費
            if clock > 0:
                clock -= 1

            # --- ペリフェラル ---
            ## LCDC
            lcdc.scan(reg, mem)

if __name__ == '__main__':
    main()

