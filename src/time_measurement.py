from time import time


class TimeMeasurement:
    start: time
    end: time

    def __init__(self):
        self.start = time()

    def stop(self):
        self.end = time()

    def get_ms(self, round_to: int = 3):
        x = (self.end - self.start) * 1000
        if round_to == -1:
            return x
        return round(x, round_to)

    def check_increase(self, other: "TimeMeasurement", round_to: int = 3):
        x = self.get_ms(round_to=-1) / other.get_ms(round_to=-1)
        if round_to is None:
            return x
        return round(x, round_to)

    def __repr__(self) -> str:
        ms = (self.end - self.start) * 1000

        if ms > 60 * 1000:
            return f'{round(ms / 1000 / 60, 3)} m'
        if ms > 1000:
            return f'{round(ms / 1000, 3)} s'
        else:
            return f'{round(ms, 3)} ms'
