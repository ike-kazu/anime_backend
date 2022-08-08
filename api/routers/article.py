from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.article as article_crud
from api.db import get_db
from typing import List

from api.schemas import article as article_schema


router = APIRouter()

@router.get("/articles", response_model=List[article_schema.Article])
async def list_articles():
    return [article_schema.Article(id=1, articleURL="https://article", imageURL="https://image")]

@router.post('/article', response_model=article_schema.ArticleCreateResponse)
async def create_article(
    article_body: article_schema.ArticleCreate, db: AsyncSession = Depends(get_db)
    ):
    return await article_crud.create_article(db, article_body)

@router.put("/articles/{article_id}", response_model=article_schema.ArticleCreateResponse)
async def update_article(article_id: int, article_body: article_schema.ArticleCreate):
    return article_schema.ArticleCreateResponse(id=article_id, **article_body.dict())

@router.delete("/articles/{article_id}", response_model=None)
async def delete_article():
    return