from contextlib import asynccontextmanager

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from .setting import setting, logger
from beanie import init_beanie
@asynccontextmanager
async def connect_to_db(app: FastAPI):
    app.db = AsyncIOMotorClient(setting.MONGO_DATABASE_URI).task_management
    await init_beanie(database=app.db, document_models=[])
    logger.success(f"Connected to database: {setting.MONGO_DATABASE}")
    yield
    logger.success(f"Disconnected from database: {setting.MONGO_DATABASE}")