from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from .models import User, engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def get_user(user_id: int) -> Optional[User]:
    async with SessionLocal() as session:
        query = select(User).where(User.id == user_id)
        result = await session.execute(query)
        user = result.scalars().first()
        return user

async def get_users() -> List[User]:
    async with SessionLocal() as session:
        query = select(User)
        result = await session.execute(query)
        users = result.scalars().all()
        return users

async def create_user(name: str, email: str) -> User:
    async with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

async def update_user(user_id: int, name: str, email: str) -> Optional[User]:
    async with SessionLocal() as session:
        query = select(User).where(User.id == user_id)
        result = await session.execute(query)
        user = result.scalars().first()
        if user:
            user.name = name
            user.email = email
            await session.commit()
            await session.refresh(user)
            return user
        return None

async def delete_user(user_id: int) -> None:
    async with SessionLocal() as session:
        query = select(User).where(User.id == user_id)
        result = await session.execute(query)
        user = result.scalars().first()
        if user:
            await session.delete(user)
            await session.commit()
