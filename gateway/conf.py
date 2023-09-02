import os

from pydantic import BaseModel


class Settings(BaseModel):
    ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES: int = 360
    USERS_SERVICE_URL: str = os.environ.get('USERS_SERVICE_URL')
    ORDERS_SERVICE_URL: str = os.environ.get('ORDERS_SERVICE_URL')
    SUPPLIERS_SERVICE_URL: str = os.environ.get('SUPPLIERS_SERVICE_URL')
    GATEWAY_TIMEOUT: int = 59


settings = Settings()
