from icecream import ic

ic.configureOutput(includeContext=True)


class Fac:
    def __init__(self):
        pass

    def fac(self, n: int) -> int:
        ic(n)
        if n == 1:
            return ic(1)
        else:
            return ic(n * self.fac(n - 1))


if __name__ == '__main__':
    f = Fac()
    print(f.fac(10))
