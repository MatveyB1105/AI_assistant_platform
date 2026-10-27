from fastapi import FastAPI
from sqlalchemy import text

from src.core.database import engine

app = FastAPI(title="AI Assistant Platform", version="0.1.0")


@app.get("/health")
async def health() -> dict:
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    return {"status": "ok"}