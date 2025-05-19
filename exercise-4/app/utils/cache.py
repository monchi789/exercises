from functools import wraps
import time


_cache = {}


def cached_response(ttl: int):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key = (func.__name__, str(args), str(kwargs))
            now = time.time()

            if key in _cache:
                value, timestamp = _cache[key]
                
                if now - timestamp < ttl:
                    return value
            
            value = await func(*args, **kwargs)
            _cache[key] = (value, now)

            return value
        
        return wrapper
    
    return decorator