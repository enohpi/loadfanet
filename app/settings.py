from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "loadfanet"

    client_netdata_url: str
    client_netdata_port: str

    class Config:
        env_file = "../.env"
