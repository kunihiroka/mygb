import mygb

import numpy as np

def f3():
    """
    DI:
    This instruction disables interrupts but not immediately.
    Interrupts are disabled after instruction DI is executed.
    """
    print('f3')

def c3():
    """
    JP nn
    Jump to address nn.
    """
    print('c3')

instruction_table = {
    "f3": f3,
    "c3": c3,
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
            data = file.read(1)          # 1byte読み出し

            instruction_table[data.hex()]()

            # プログラムカウンタを進める
            pc = pc + 1


if __name__ == '__main__':
    main()

