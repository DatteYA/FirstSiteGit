from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Text
from .mixfin import Relation_user_id


class Profile(Base, Relation_user_id):
    user_back_populates = "profile"
    unique = True

    first_name: Mapped[str | None] = mapped_column(String(25))
    last_name: Mapped[str | None] = mapped_column(String(25))
    bio: Mapped[str | None] = mapped_column(Text(100))
    
    
