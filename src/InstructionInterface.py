from abc import ABC, abstractmethod
# 命令の抽象クラス
class MyInterface(ABC):
    @abstractmethod
    def getParameterSize(self):
        pass

    @abstractmethod
    def execute(self, parameter, register):
        pass
