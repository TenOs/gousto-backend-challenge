from fastapi import APIRouter

from models.database import RecipeDatabase
from models.recipe import Recipe, RecipeListResponse, RecipeUpdateRequest
from utils import load_csv_data

router = APIRouter()


_recipe_db = RecipeDatabase(load_csv_data('recipe-data.csv'))


@router.get('/', response_model=RecipeListResponse)
async def search_recipes(
        cuisine: str, offset: int = 0, nb: int = 10
):
    """
    Searches recipes.

    Currently only the search by cuisine is supported.

    :param cuisine: cuisine type to filter
    :param offset: offset of results to fetch
    :param nb: number of results to return
    :return: list of recipes
    """
    if nb > 10 or nb < 0:
        nb = 10

    res, total = _recipe_db.search(
        cuisine=cuisine,
        nb_results=nb,
        offset=offset
    )
    nb_res = len(res)

    return RecipeListResponse(
        total=total,
        next_offset=offset + nb_res if offset + nb_res < total else None,
        data=res
    )


@router.get('/{recipe_id}', response_model=Recipe)
async def get_by_id(recipe_id: int):
    """
    Gets a Recipe by it's id.

    :param recipe_id: id of the Recipe to fetch
    :return: corresponding Recipe
    """
    return _recipe_db.get_recipe(recipe_id)


@router.patch('/{recipe_id}', response_model=Recipe)
async def update_recipe(recipe_id: int, data: RecipeUpdateRequest):
    """
    Updates a Recipe.

    :param recipe_id: id of the Recipe to update
    :param data: dictionary of updates to perform
    :return: updated Recipe
    """
    return _recipe_db.update_recipe(recipe_id, data.dict(skip_defaults=True))
