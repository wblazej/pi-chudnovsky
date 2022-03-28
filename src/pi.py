import math

class PI:
    digits: int

    def __init__(self, digits: int):
        self.digits = digits
        self.c = 640320
        self.c3_over_24 = self.c ** 3 // 24
        self.one = 10 ** digits

    def calc(self):
        N = int(self.digits / math.log10(self.c3_over_24 / 6 / 2 / 6) + 1)
        _, Q, T = self.bs(0, N)
        sqrtC = self.sqrt(10005 * self.one)
        return (Q * 426880 * sqrtC) // T

    def bs(self, a, b):
        if b - a == 1:
            if a == 0:
                Pab = Qab = 1
            else:
                Pab = (6 * a - 5) * (2 * a - 1) * (6 * a - 1)
                Qab = a ** 3 * self.c3_over_24
            Tab = Pab * (13591409 + 545140134 * a)

            if a & 1:
                Tab = -Tab
        else:
            m = (a + b) // 2
            Pam, Qam, Tam = self.bs(a, m)
            Pmb, Qmb, Tmb = self.bs(m, b)
            Pab = Pam * Pmb
            Qab = Qam * Qmb
            Tab = Qmb * Tam + Pam * Tmb
        return Pab, Qab, Tab

    def sqrt(self, n):
        floating_point_precision = 10 ** 16
        n_float = float((n * floating_point_precision) // self.one) / floating_point_precision
        x = (int(floating_point_precision * math.sqrt(n_float)) * self.one) // floating_point_precision
        n_one = n * self.one

        while True:
            x_old = x
            x = (x + n_one // x) // 2

            if x == x_old:
                break

        return x