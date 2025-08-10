import uuid
from datetime import date, datetime
from typing import List, Optional

import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Date, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Mapped, mapped_column

Base = declarative_base()

# Association table for many-to-many relationship between books and tags
book_tags = Table(
    'book_tags',
    Base.metadata,
    Column('book_id', pg.UUID, ForeignKey('books.uid'), primary_key=True),
    Column('tag_id', pg.UUID, ForeignKey('tags.uid'), primary_key=True)
)

class User(Base):
    __tablename__ = "users"
    
    uid: Mapped[uuid.UUID] = mapped_column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(pg.VARCHAR, nullable=False, server_default="user")
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    password_hash: Mapped[str] = mapped_column(pg.VARCHAR, nullable=False)
    created_at: Mapped[datetime] = mapped_column(pg.TIMESTAMP, default=datetime.now)
    update_at: Mapped[datetime] = mapped_column(pg.TIMESTAMP, default=datetime.now)
    
    # Relationships
    books: Mapped[List["Book"]] = relationship(
        back_populates="user", lazy="selectin"
    )
    reviews: Mapped[List["Review"]] = relationship(
        back_populates="user", lazy="selectin"
    )

    def __repr__(self):
        return f"<User {self.username}>"


class Book(Base):
    __tablename__ = "books"
    
    uid: Mapped[uuid.UUID] = mapped_column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    publisher: Mapped[str] = mapped_column(String, nullable=False)
    published_date: Mapped[date] = mapped_column(Date, nullable=False)
    page_count: Mapped[int] = mapped_column(Integer, nullable=False)
    language: Mapped[str] = mapped_column(String, nullable=False)
    user_uid: Mapped[Optional[uuid.UUID]] = mapped_column(pg.UUID, ForeignKey("users.uid"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(pg.TIMESTAMP, default=datetime.now)
    update_at: Mapped[datetime] = mapped_column(pg.TIMESTAMP, default=datetime.now)
    
    # Relationships
    user: Mapped[Optional["User"]] = relationship(back_populates="books")
    reviews: Mapped[List["Review"]] = relationship(
        back_populates="book", lazy="selectin"
    )
    tags: Mapped[List["Tag"]] = relationship(
        secondary=book_tags, back_populates="books", lazy="selectin"
    )

    def __repr__(self):
        return f"<Book {self.title}>"


class Review(Base):
    __tablename__ = "reviews"
    
    uid: Mapped[uuid.UUID] = mapped_column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    review_text: Mapped[str] = mapped_column(pg.VARCHAR, nullable=False)
    user_uid: Mapped[Optional[uuid.UUID]] = mapped_column(pg.UUID, ForeignKey("users.uid"), nullable=True)
    book_uid: Mapped[Optional[uuid.UUID]] = mapped_column(pg.UUID, ForeignKey("books.uid"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(pg.TIMESTAMP, default=datetime.now)
    update_at: Mapped[datetime] = mapped_column(pg.TIMESTAMP, default=datetime.now)
    
    # Relationships
    user: Mapped[Optional["User"]] = relationship(back_populates="reviews")
    book: Mapped[Optional["Book"]] = relationship(back_populates="reviews")

    def __repr__(self):
        return f"<Review for book {self.book_uid} by user {self.user_uid}>"


class Tag(Base):
    __tablename__ = "tags"
    
    uid: Mapped[uuid.UUID] = mapped_column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(pg.VARCHAR, nullable=False)
    created_at: Mapped[datetime] = mapped_column(pg.TIMESTAMP, default=datetime.now)
    
    # Relationships
    books: Mapped[List["Book"]] = relationship(
        secondary=book_tags, back_populates="tags", lazy="selectin"
    )

    def __repr__(self) -> str:
        return f"<Tag {self.name}>"
