import functools
import time
from typing import Callable


def measure_time(f):
    """Decorator measure time taken to execute function"""

    @functools.wraps(f)
    def wrap(*args, **kwargs):

        start_time = time.time()
        x = f(*args, **kwargs)
        end_time = time.time()

        print(f"Time taken: {end_time - start_time} seconds")
        return x

    return wrap
