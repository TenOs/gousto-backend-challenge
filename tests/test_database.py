import pytest
from models.database import RecipeDatabase
from models.exceptions import RecipeNotFoundException


def test_initialize(recipes):
    database = RecipeDatabase(recipes)
    assert len(database._recipes_by_id.values()) == len(recipes)


def test_get_recipe(recipe_database: RecipeDatabase):
    recipe = recipe_database.get_recipe(1)
    assert recipe.id == 1


def test_get_recipe_not_found(recipe_database: RecipeDatabase):
    with pytest.raises(RecipeNotFoundException):
        recipe_database.get_recipe(99999)


def test_search_all(recipe_database: RecipeDatabase):
    results, nb_total = recipe_database.search('british')
    assert len(results) == 4
    assert nb_total == 4


def test_search_no_result(recipe_database: RecipeDatabase):
    results, nb_total = recipe_database.search('no-result')
    assert nb_total == 0
    assert len(results) == 0


def test_search_pagination(recipe_database: RecipeDatabase):
    results, nb_total = recipe_database.search('british', nb_results=2)
    assert nb_total == 4
    assert len(results) == 2

    results, nb_total = recipe_database.search('british', nb_results=2, offset=2)
    assert nb_total == 4
    assert len(results) == 2

    results, nb_total = recipe_database.search('british', nb_results=2, offset=4)
    assert nb_total == 4
    assert len(results) == 0

    results, nb_total = recipe_database.search('british', nb_results=10)
    assert nb_total == 4
    assert len(results) == 4


def test_update(recipe_database: RecipeDatabase):
    updated_recipe = recipe_database.update_recipe(1, {'title': 'new title'})
    assert updated_recipe.id == 1
    assert updated_recipe.title == 'new title'


def test_update_not_found(recipe_database: RecipeDatabase):
    with pytest.raises(RecipeNotFoundException):
        recipe_database.update_recipe(999, {'title': 'test'})
