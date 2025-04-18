from .base import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import String, Text, ForeignKey
from .mixfin import Relation_user_id


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User

class Post(Base, Relation_user_id):
    user_back_populates = "posts"
    title: Mapped[int] = mapped_column(String(40), unique=False)
    body: Mapped[str] = mapped_column(Text(5000), default="", server_default="")
    
    