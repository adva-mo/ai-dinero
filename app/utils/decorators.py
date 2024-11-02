from functools import wraps
from typing import Callable, Any


def handle_single_or_list(func: Callable[..., Any]):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Find the first Pydantic model in kwargs
        for key, value in kwargs.items():
            if hasattr(value, '__pydantic_model__'):
                if not isinstance(value, list):
                    kwargs[key] = [value]
                break
        return await func(*args, **kwargs)
    return wrapper
