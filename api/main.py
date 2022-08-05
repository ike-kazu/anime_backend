from fastapi import FastAPI
from api.routers import article


app = FastAPI() # FastAPIはStarletteを直接継承するクラスです。
app.include_router(article.router)