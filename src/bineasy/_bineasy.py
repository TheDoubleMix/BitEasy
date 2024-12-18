from typing import Self, Sequence, Union, TypeAlias
Bits: TypeAlias = Sequence[Union["0", "1"]]
class BitString:
    def __init__(self, bits: Bits) -> None:
        self.bits = bits
        pass
    def __repr__(self) -> Self:
        return BitString(self.bits)
    def ConvertToInt(self) -> int:
        return int(self.bits, 2)
    def ConvertToBytes(self) -> bytes:
        return bytes(int(self.bits[i : i + 8], 2) for i in range(0, len(self.bits), 8))
    def ConvertToStr(self, encoding: str = "UTF-8") -> str:
        return str(self.ConvertToBytes(), encoding)
class readfrom:
    class file: 
        def __init__(self, file: str) -> None:
            with open(file, 'rb') as f:
                _bytes = f.read()
            self.bitstr = ''.join(f'{z:08b}' for z in _bytes)
            pass
        def readbits(self, offset: int, amount: int) -> BitString:
            return BitString(self.bitstr[offset:offset+amount])
    class bytes:
        def __init__(self, _bytes: bytes) -> None:
            self.bitstr = ''.join(f'{z:08b}' for z in _bytes)
            pass
        def readbits(self, offset: int, amount: int) -> BitString:
            return BitString(self.bitstr[offset:offset+amount])