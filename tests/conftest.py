from typing import Generator

import pytest
from fastapi.testclient import TestClient

from src.todoapp.main import app


@pytest.fixture()
def test_app() -> Generator:
    with TestClient(app) as _client:
        yield _client
