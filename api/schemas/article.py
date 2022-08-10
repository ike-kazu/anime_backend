from typing import Optional, List

from pydantic import BaseModel, Field


class ArticleBase(BaseModel):
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

class ArticlesCreate(BaseModel):
    articles: List[ArticleBase]