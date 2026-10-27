import asyncio

import asyncpg

from src.core.config import get_settings

import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main() -> None:
    s = get_settings()
    conn = await asyncpg.connect(
        host="127.0.0.1",
        port=s.postgres_port,
        user=s.postgres_user,
        password=s.postgres_password,
        database=s.postgres_db,
        timeout=15,
    )
    print("OK:", await conn.fetchval("SELECT version()"))
    await conn.close()


asyncio.run(main())