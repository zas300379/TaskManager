from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.core import Config


# --- Конфиги
ASYNC_DATABASE_URL = Config.ASYNC_DATABASE_URL

# --- Базовая модель
Base = declarative_base()

# --- АСИНХРОННЫЙ движок и сессия
async_engine = create_async_engine(ASYNC_DATABASE_URL, echo=False, future=True)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False
)


async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
