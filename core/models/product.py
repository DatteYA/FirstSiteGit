from .base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Product(Base):
    name: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
