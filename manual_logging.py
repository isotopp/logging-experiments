import functools


def args_to_str(*args):
    return ", ".join(map(str, args))


def kwargs_to_str(**kwargs):
    ret = ""
    for k, v in kwargs.items():
        ret += f"{k}={v},"

    return ret[:-1]


def logging(func):
    func.__indent__ = 0

    @functools.wraps(func)
    def wrapper_logging(*args, **kwargs):
        func_indent = " " * func.__indent__
        func.__indent__ += 2

        func_name = func.__name__
        func_args = args_to_str(*args)
        func_kwargs = kwargs_to_str(**kwargs)

        print(f"{func_indent} -> Enter: {func_name}({func_args}", end="")
        if func_kwargs != "":
            print(f", {func_kwargs}", end="")
        print(")")

        result = func(*args, **kwargs)

        print(f"{func_indent} <- Leave: {func_name}({result})")
        return result

    return wrapper_logging


@logging
def fac(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


if __name__ == '__main__':
    result = fac(3)
    print(f"{result=}")
