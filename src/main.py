import numpy as np

def main():
    print('hello world')
    # レジスタ定義
    pc = np.uint16(0)

    # ROMファイルの読み込み
    with open('../rom/hello-world.gb', 'rb') as file: # 'rb'で開くとバイナリ読み込みになる。
        pc = int('100', 16)

        file.seek(pc)
        data = file.read(1)
        print(data)

        if data == b'\xf3':
            f3()

        # プログラムカウンタを進める
        pc = pc + 1

        file.seek(pc)
        data = file.read(1)
        print(data)

        if data == b'\xc3'
            c3()

def f3():
    print('Interrupts disabled')

if __name__ == '__main__':
    main()

