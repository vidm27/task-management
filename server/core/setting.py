import secrets
from pathlib import Path
from typing import List, Optional, Any, Union

from loguru import logger as lugu_logger
from pydantic import field_validator, FieldValidationInfo
from pydantic.networks import MongoDsn, AnyHttpUrl
from pydantic_settings import BaseSettings


# export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

class Setting(BaseSettings):
    API_V1_STR: str = "/api"
    SECRET_KEY: str = secrets.token_urlsafe(23)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    BACKEND_CORS_ORIGINS: List
    PROJECT_NAME: str
    UPLOAD_DIR: Path

    MONGO_USERNAME: str
    MONGO_PASSWORD: str
    MONGO_DATABASE: str
    MONGO_PORT: str
    MONGO_HOST: str
    MONGO_QUERY: str
    MONGO_DATABASE_URI: Optional[Union[MongoDsn, str]] = None

    @field_validator("MONGO_DATABASE_URI")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], values: FieldValidationInfo) -> Any:
        if isinstance(v, str):
            return v
        uri = MongoDsn.build(
            scheme="mongodb",
            username=values.data.get("MONGO_USERNAME"),
            password=values.data.get("MONGO_PASSWORD"),
            host=values.data.get("MONGO_HOST"),
            port=int(values.data.get("MONGO_PORT")),
            path=values.data.get("MONGO_DATABASE"),
            query=values.data.get("MONGO_QUERY")
        )
        # print(f"URI MONGO: {uri}")
        return str(uri)

    class Config:
        case_sensitive = True


def path_upload_dir() -> Path:
    parent_dir = Path(__file__).resolve().parent.parent
    return parent_dir / 'upload'


setting = Setting(
    SERVER_HOST="http://127.0.0.1",
    SERVER_NAME="waster-way",
    PROJECT_NAME="waster-way",
    MONGO_USERNAME="waste_way",
    MONGO_PASSWORD="waste_way",
    MONGO_DATABASE="waste_way",
    MONGO_PORT="27017",
    MONGO_HOST="127.0.0.1",
    MONGO_QUERY="authSource=admin",
    BACKEND_CORS_ORIGINS=["*"],
    UPLOAD_DIR=path_upload_dir()
)

logger = lugu_logger
