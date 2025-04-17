from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status, Depends, Path
from . import crud
from core.models import Product, db_helper
from typing import Annotated


async def get_product_byid(
    product_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Product:
    product = await crud.get_product(session=session, product_id=product_id)
    if product is not None:
        return product
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_id} not found. Try to again with another id",
        )
