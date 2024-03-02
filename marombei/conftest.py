import pytest

from typing import Generator

from django.contrib.auth import get_user_model


UserModel = get_user_model()


@pytest.fixture
def superuser() -> Generator[dict[str:str], None, None]:
    credentials = {"username": "usertest", "password": "passtest"}

    user = UserModel.objects.create_superuser(**credentials)

    yield credentials

    user.delete()
