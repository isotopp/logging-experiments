from snoop import snoop, spy

@snoop
def fac(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * fac(n-1)

if __name__ == '__main__':
    result = fac(3)
    print(f"{result=}")
