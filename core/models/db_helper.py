from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)
from core.config import settings
from asyncio import current_task


class DatabaseHelper:
    def __init__(self, url, echo):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scopped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def scoped_session_dependency(self):
        session_p = self.get_scopped_session()
        session = session_p()
        try:
            yield session
        finally:
            await session_p.remove()


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)
