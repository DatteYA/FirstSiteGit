from .base import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import String, Text, ForeignKey



from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User

class Post(Base):
    title: Mapped[int] = mapped_column(String(40), unique=False)
    body: Mapped[str] = mapped_column(Text(5000), default="", server_default="")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="posts")