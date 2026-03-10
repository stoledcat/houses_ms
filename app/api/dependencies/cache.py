from typing import Annotated, TypeAlias

from fastapi import Depends
from redis.asyncio import Redis
from fastapi import Request


def get_cache(request: Request) -> Redis:
    return request.app.state.redis


CacheDep = Annotated[Redis, Depends(get_cache)]
