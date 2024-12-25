def fibonacci(n: int | None = ...) -> int:

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(n=8)
