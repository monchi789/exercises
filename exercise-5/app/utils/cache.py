from cachetools import TTLCache


user_cache = TTLCache(maxsize=1, ttl=300)