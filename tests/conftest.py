from typing import List

import pytest

from models.database import RecipeDatabase
from utils import load_csv_data
from starlette.testclient import TestClient


@pytest.fixture
def recipes() -> List[dict]:
    return load_csv_data('recipe-data.csv')


@pytest.fixture
def recipe_database(recipes) -> RecipeDatabase:
    return RecipeDatabase(recipes)


@pytest.fixture
def test_client() -> TestClient:
    from main import app
    return TestClient(app)
