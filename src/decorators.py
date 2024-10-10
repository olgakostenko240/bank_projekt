from collections.abc import Callable
from functools import wraps
from typing import Any


def log(filename: str | None) -> Callable:
    """Дукоратор логирует начало и конец выполнения декорируемой функции"""

    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                # time_1 = time()
                result = func(*args, **kwargs)
                # time_2 = time()
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
            return Exception

        return inner

    return wrapper


@log(filename="my_log.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
