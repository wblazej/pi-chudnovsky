class ReadPI:
    def __init__(self, filename: str):
        self.pi = open(filename, 'r')

    def read(self, _to: int, _from: int = 0):
        if _from < 0:
            _from = 0

        if _from > _to:
            _from, _to = _to, _from

        self.pi.seek(_from + 2)
        return self.pi.read(_to - _from)
