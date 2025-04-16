from read_rom import read_rom
import os

def test_read_rom():
    rom_path = os.path.abspath('./tests/rsc/hello-world.gb')
    assert read_rom(rom_path) == 0

