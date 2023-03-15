from peepshow import peep

def fac(n: int) -> int:
    peep()
    if n <= 1:
        return 1
    else:
        return n * fac(n-1)

if __name__ == '__main__':
    result = fac(3)
    print(f"{result=}")
