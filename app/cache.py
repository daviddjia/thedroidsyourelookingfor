from redis_dec import Cache
from redis import StrictRedis

redis = StrictRedis(host='redis', port=6379, decode_responses=True)
cache = Cache(redis)
