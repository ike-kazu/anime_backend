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

async def create_articles(
    db: AsyncSession, articles_create: article_schema.ArticlesCreate
) -> article_model.Article:
    # debug
    print(articles_create.articles)
    for article in articles_create.dict()["articles"]:
        article = article_model.Article(**article)
        db.add(article)
        await db.commit()
        await db.refresh(article)
    return articles_create.dict()