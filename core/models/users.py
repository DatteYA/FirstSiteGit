from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .posts import Post
    from .profile import Profile

class User(Base):
    nickname: Mapped[int] = mapped_column(String(20), unique=True)
    
    posts: Mapped["list[Post]"] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")

