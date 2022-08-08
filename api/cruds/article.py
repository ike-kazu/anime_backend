from sqlalchemy.ext.asyncio import AsyncSession

import api.models.article as article_model
import api.schemas.article as article_schema


async def create_article(
    db: AsyncSession, article_create: article_schema.ArticleCreate
) -> article_model.Article:
    article = article_model.Article(**article_create.dict())
    db.add(article)
    await db.commit()
    await db.refresh(article)
    return article