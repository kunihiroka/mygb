from abc import ABC, abstractmethod
# 命令の抽象クラス
class MyInterface(ABC):
    @abstractmethod
    def getParameterSize(self, opcode):
        pass

    @abstractmethod
    def execute(self, opcode, parameter, register, memory):
        pass
