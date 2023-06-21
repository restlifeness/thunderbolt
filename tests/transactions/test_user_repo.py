import sys
import pytest

from pathlib import Path

from sqlalchemy import select

sys.path.append(str(Path.cwd()))

from thunderbolt.models.user import User
from thunderbolt.user.repository import UserRepository

from tests.fixtures.db import mock_session


@pytest.mark.asyncio
async def test_user_creation(mock_session):
    async with mock_session() as mock_session:
        user_repo = UserRepository(mock_session)
        mock_username = 'test_user'

        user = User(
            username=mock_username,
            email='example@gmail.com'
        )
        user.password = 'test_password'

        await user_repo.add(user)

        stmt = select(User).where(User.username == mock_username)
        result = await mock_session.execute(stmt)
        user = result.scalars().first()

        assert user.username == mock_username


@pytest.mark.asyncio
async def test_user_update(mock_session):
    async with mock_session() as session:
        user_repo = UserRepository(session)
        user = User(username='test', email='test@gmail.com')
        user.password = 'password'

        await user_repo.add(user)

        user.username = 'updated_test'
        await user_repo.update(user)

        stmt = select(User).where(User.username == 'updated_test')
        result = await session.execute(stmt)
        updated_user = result.scalars().first()

        assert updated_user.username == 'updated_test'


@pytest.mark.asyncio
async def test_get_user(mock_session):
    async with mock_session() as session:
        user_repo = UserRepository(session)
        user = User(username='test', email='test@gmail.com')
        user.password = 'password'

        await user_repo.add(user)

        retrieved_user = user_repo.get(user.id)

        assert retrieved_user == user


@pytest.mark.asyncio
async def test_get_user_by_username(mock_session):
    async with mock_session() as session:
        user_repo = UserRepository(session)
        user = User(username='test', email='test@gmail.com')
        user.password = 'password'

        await user_repo.add(user)

        retrieved_user = user_repo.get_by_username(user.username)

        assert retrieved_user == user


@pytest.mark.asyncio
async def test_get_user_by_email(mock_session):
    async with mock_session() as session:
        user_repo = UserRepository(session)
        user = User(username='test', email='test@gmail.com')
        user.password = 'password'

        await user_repo.add(user)

        retrieved_user = user_repo.get_by_email(user.email)

        assert retrieved_user == user


@pytest.mark.asyncio
async def test_get_all_users(mock_session):
    async with mock_session() as session:
        user_repo = UserRepository(session)
        users = [User(username=f'user{i}', email=f'user{i}@gmail.com') for i in range(5)]
        
        for user in users:
            user.password = 'password'
            await user_repo.add(user)

        all_users = user_repo.get_all()

        assert len(all_users) == 5


@pytest.mark.asyncio
async def test_delete_user(mock_session):
    async with mock_session() as session:
        user_repo = UserRepository(session)
        user = User(username='test', email='test@gmail.com')
        user.password = 'password'

        await user_repo.add(user)
        await user_repo.delete(user)

        stmt = select(User).where(User.username == 'test')
        result = await session.execute(stmt)
        deleted_user = result.scalars().first()

        assert deleted_user is None
