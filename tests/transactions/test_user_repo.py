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
