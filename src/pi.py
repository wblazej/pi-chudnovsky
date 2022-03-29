import math


class PI:
    digits: int

    def __init__(self, digits: int):
        self.digits = digits
        self.c = 640320
        self.c3_over_24 = self.c ** 3 // 24
        self.one = 10 ** digits

    def calc(self):
        n = int(self.digits / math.log10(self.c3_over_24 / 6 / 2 / 6) + 1)
        _, q, t = self.bs(0, n)
        sqrt_c = self.sqrt(10005 * self.one)
        return (q * 426880 * sqrt_c) // t

    def bs(self, a, b):
        if b - a == 1:
            if a == 0:
                pab = qab = 1
            else:
                pab = (6 * a - 5) * (2 * a - 1) * (6 * a - 1)
                qab = a ** 3 * self.c3_over_24
            tab = pab * (13591409 + 545140134 * a)

            if a & 1:
                tab = -tab
        else:
            m = (a + b) // 2
            pam, qam, tam = self.bs(a, m)
            pmb, qmb, tmb = self.bs(m, b)
            pab = pam * pmb
            qab = qam * qmb
            tab = qmb * tam + pam * tmb
        return pab, qab, tab

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
