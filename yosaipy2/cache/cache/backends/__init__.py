from yosaipy2.cache.cache.region import register_backend

register_backend("yosaipy2.cache.redis", "yosaipy2.cache.cache.backends.redis", "RedisBackend")
