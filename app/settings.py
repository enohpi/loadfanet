from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "loadfanet"

    client_netdata_url: str
    client_netdata_port: str

    client_netdata_timeout_sec: int  # Таймаут ожидания ответа от сервиса
    client_netdata_retries: int  # Количество попыток запросов к внешнему сервису
    client_netdata_wait_sec: int  # Время ожидания между попытками client_nalog_retries

    class Config:
        env_file = "../.env"
