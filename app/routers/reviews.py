from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, update

from app.models.reviews import Review as ReviewModel
from app.schemas import Review as ReviewSchema, ReviewCreate

from app.models.users import User as UserModel
from app.auth import get_current_seller             #------authentification!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from sqlalchemy.ext.asyncio import AsyncSession

from app.db_depends import get_async_db


router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],
)

@router.get("/", response_model=list[ReviewSchema], status_code=status.HTTP_200_OK)
async def get_all_reviews(db: AsyncSession = Depends(get_async_db())):
    """
    Возвращает список всех активных отзывов.
    """
    reviews_result = await db.scalars(
        select(ReviewModel).where(ReviewModel.is_active == True)
    )
    reviews = reviews_result.all()
    return reviews


