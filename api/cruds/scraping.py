import api.scraping.animeanime as animeanime_scraping
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.article as article_model
import api.schemas.article as article_schema
import api.scraping.animeanime as article_animeanime
import asyncio
from sqlalchemy.engine import Result
from sqlalchemy import select
from typing import List, Tuple


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


async def get_article_latest(db: AsyncSession) -> List[Tuple[int, str, str]]:
    result: Result = await (
        db.execute(
            select(
                article_model.Article.id,
                article_model.Article.imageURL,
                article_model.Article.articleURL,
            ).order_by(article_model.Article.id.desc()).limit(1)
        )
    )
    return result.all()


async def create_articles(
    db: AsyncSession, articles_create: article_schema.ArticlesCreate
) -> article_model.Article:

    # get latest article data
    latest_article =await get_article_latest(db)

    # debug
    articles = article_animeanime.scraping()
    print("articles = ", articles)
    print("length = ", len(articles))

    # 新しい記事の選別
    new_article = []
    print("latest_article = ", latest_article[0][2])
    print("article = ", articles)
    for article in articles:
        print("article[articleURL] = ", article["articleURL"])
        if article["articleURL"] == latest_article[0][2]:
            print("break")
            break
        new_article.append(article)

    print("new_article = ", new_article)
    for article in reversed(new_article):
        article = article_model.Article(**article)
        db.add(article)
        await db.commit()
        await db.refresh(article)
    return articles_create.dict()