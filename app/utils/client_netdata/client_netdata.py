import http

import aiohttp
import asyncio
from app.serializers.netdata_api_serializer import NetdataApiRequestSerializer

# url = "http://mars.evi:19999/api/v1/data?chart=services.mem_usage&dimension=eltex-videoserver&after=-480&points=3&options=ms%7Cflip%7Cnonzero&format=json&group=average&gtime=0"
url_2 = "http://mars.evi:19999"

param = NetdataApiRequestSerializer()
print(param.__annotations__)
print(param.dict())


async def main():
    async with aiohttp.ClientSession(url_2) as session:
        params = NetdataApiRequestSerializer().dict()
        async with session.get("/api/v1/data", params=params) as resp:
            print(resp.status)
            print(await resp.text())


asyncio.run(main())
