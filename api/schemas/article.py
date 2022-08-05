from typing import Optional

from pydantic import BaseModel, Field


class ArticleBase(BaseModel):
    id: int
    articleURL: Optional[str] = Field(None, example="https://articleurl")
    imageURL: Optional[str] = Field(None, example="https::/imageurl")


class ArticleCreate(ArticleBase):
    pass


class ArticleCreateResponse(ArticleCreate):
    id: int

    class Config:
        orm_mode = True


class Article(ArticleBase):
    pass