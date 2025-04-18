from sqlalchemy.orm import Mapped, relationship, mapped_column, declared_attr
from sqlalchemy import String, Text, ForeignKey


class Relation_user_id:
    user_back_populates: str | None = None
    unique: bool = False
    nullable: bool = False

    @declared_attr
    def user_id(cls):
        return mapped_column(
            ForeignKey("users.id"), nullable=cls.nullable, unique=cls.unique
        )

    @declared_attr
    def user(cls):
        return relationship("user", back_populates=cls.user_back_populates)
