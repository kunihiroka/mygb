def read_rom(path):
    """
    ROMを静的変数にロードし、静的変数のアドレスを返す。

    """
    # ROMファイルの読み込み
    with open(path, 'rb') as file: # 'rb'で開くとバイナリ読み込みになる。
        data = file.read()
        print(data)
    return 0
