import http

import aiohttp
import asyncio

url = "http://mars.evi:19999/api/v1/data?chart=services.mem_usage&dimension=eltex-videoserver&after=-480&points=3&options=ms%7Cflip%7Cnonzero&format=json&group=average&gtime=0"


class NetdataApiClient:

    def __int__(self, client_netdata_url, client_netdata_port):
        self.client_netdata_url = client_netdata_url

    async def get_data_from_netdata_api(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print(resp.status)
                print(await resp.json())


    asyncio.run(get_data_from_netdata_api())
