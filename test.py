import argparse
from src.pi import PI
from src.time_measurement import TimeMeasurement


def make_test(_min: int, _max: int, _dec: bool):
    previous = None
    base = 2 if not _dec else 10

    for i in range(_min, _max + 1):
        digits = base ** i

        tm = TimeMeasurement()
        PI(digits).calc()
        tm.stop()

        increase = None
        if previous is not None:
            increase = tm.check_increase(previous)
        previous = tm

        print('digits: {}\ttime: {:12}increase: {}'.format(digits, tm.__repr__(), increase))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--min', help='Start of testing range', type=int, required=False, default=10)
    parser.add_argument('--max', help='End of testing range', type=int, required=False, default=17)
    parser.add_argument('--dec', help='Test power of 10', action='store_true')
    args = parser.parse_args()
    make_test(args.min, args.max, args.dec)

