from src.pi import PI
from src.time_measurement import TimeMeasurement

previous = None

for i in range(10, 20):
    digits = 2 ** i

    tm = TimeMeasurement()
    PI(digits).calc()
    tm.stop()

    increase = None
    if previous is not None:
        increase = tm.check_increase(previous)
    previous = tm

    print('digits: {}\ttime: {:12}increase: {}'.format(digits, tm.__repr__(), increase))
