import logging
import sys
from autologging import logged, traced, TRACE

logging.basicConfig(
    level=TRACE,
    stream=sys.stdout,
    format="%(levelname)s:%(name)s:%(funcName)s:%(message)s"
)


@logged
@traced
class Fac:
    def __init__(self):
        pass

    def fac(self, n: int) -> int:
        self.__log.debug("OHAI")

        if n == 1:
            return 1
        else:
            return n * self.fac(n - 1)


if __name__ == '__main__':
    f = Fac()
    print(f.fac(10))
