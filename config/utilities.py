import redis
from . import settings


redis_instance = redis.Redis(
    host=settings.REDIS_HOST, 
    port=settings.REDIS_PORT, 
    decode_responses=True,
    encoding="utf-8",
    )
