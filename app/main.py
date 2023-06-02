import logging
import uvicorn
from fastapi import FastAPI, Depends
from app.settings import Settings

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
app = FastAPI()

settings = Settings()


@app.get("/")
async def root():
    return {
        "url": settings.client_netdata_url,
        "port": settings.client_netdata_port
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080)
