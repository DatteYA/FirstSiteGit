from . import crud
from .schemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial
from fastapi import APIRouter, HTTPException, status, Depends
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from .dependecies import get_product_byid


router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}", response_model=Product)
async def get_product(product: Product = Depends(get_product_byid)):
    return product


@router.put("/{product_id}", response_model=Product, response_model_exclude_unset=True)
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(get_product_byid),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_product(
        session=session, product=product, ProductUpdate=product_update
    )


@router.patch(
    "/{product_id}", response_model=Product, response_model_exclude_unset=True
)
async def update_product(
    product_update: ProductUpdatePartial,
    product: Product = Depends(get_product_byid),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_product(
        session=session, product=product, ProductUpdate=product_update, partial=True
    )


@router.delete("/{product_id}")
async def delete_product(
    product: Product = Depends(get_product_byid),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    return await crud.delete_product(session=session, product=product)
