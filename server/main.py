from fastapi import FastAPI
from core.setting import setting
from core.db_connection import connect_to_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=setting.PROJECT_NAME,
    version=setting.VERSION,
    lifespan=connect_to_db
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=setting.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)