import api.scraping.animeanime as animeanime_scraping
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.article as article_model
import api.schemas.article as article_schema
import api.scraping.animeanime as article_animeanime


async def create_article(
    db: AsyncSession, article_create: article_schema.ArticleCreate
) -> article_model.Article:
    article = article_model.Article(**article_create.dict())
    db.add(article)
    await db.commit()
    await db.refresh(article)
    return article


async def scraping_articles(
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
    articles = article_animeanime.scraping()
    print("articles = ", articles)
    print("length = ", len(articles))
    for article in articles:
        article = article_model.Article(**article)
        db.add(article)
        await db.commit()
        await db.refresh(article)
    return articles_create.dict()