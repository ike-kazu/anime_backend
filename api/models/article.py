from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    imageURL = Column(String(1024))

    articleURL = Column(String(1024))
    # done = relationship("Done", back_populates="task")
