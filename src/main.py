def main():
    print('hello world')

    # ROMファイルの読み込み
    with open('./rom/hello-world.gb', 'rb') as file: # 'rb'で開くとバイナリ読み込みになる。
        data = file.read()
        print(data)

if __name__ == '__main__':
    main()

