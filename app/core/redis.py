""" Module for Redis initialization and operations """

from redis.asyncio import ConnectionPool, Redis

from app.core import settings

pool = ConnectionPool.from_url(settings.REDIS_URL)
redis = Redis(connection_pool=pool)
