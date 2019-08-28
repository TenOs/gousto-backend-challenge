from collections import defaultdict
from copy import deepcopy
from datetime import datetime
from typing import List, Tuple

from models.exceptions import RecipeNotFoundException
from models.recipe import Recipe
from dateutil.parser import parse


class RecipeDatabase:
    """
    This is a Dabatase like class. It simulates CRUD operations on recipes.
    It also stores data in map to provide an easy and constant access.
    Time complexity for access and updates is constant.
    """

    def __init__(self, data: List[dict]) -> None:
        """
        Initializes a RecipeDatabase instance.

        :param data: list of recipes to store
        """
        super().__init__()

        # parse the dates to store them as datetime objects
        for recipe in data:
            recipe.update({
                'created_at': parse(recipe['created_at']),
                'updated_at': parse(recipe['updated_at']),
            })

        recipes = [
            Recipe(**recipe_data)
            for recipe_data in data
        ]

        # provides a constant reading & updating time
        self._recipes_by_id = {
            recipe.id: recipe
            for recipe in recipes
        }

        # allows an easy filtering on recipes by cuisine
        self._recipes_by_cuisine = defaultdict(list)
        for recipe in recipes:
            self._recipes_by_cuisine[recipe.recipe_cuisine].append(recipe)

    def get_recipe(self, recipe_id: int) -> Recipe:
        """
        Gets a recipe by it's id.

        Throws a RecipeNotFoundException if no recipe is found.

        :param recipe_id: recipe_id of the recipe to fetch
        :return: corresponding Recipe
        """
        try:
            return self._recipes_by_id[recipe_id]
        except KeyError:
            raise RecipeNotFoundException

    def search(
            self, cuisine: str, nb_results: int = 0, offset: int = 0
    ) -> Tuple[List[Recipe], int]:
        """
        Searches recipes by cuisine type.

        Later on this function should be extended to support
        filtering on any fields.

        :param cuisine: cuisine type to filter
        :param nb_results: number of recipes to return
        :param offset: offset of recipes to return
        :return: list of Recipe
        """
        res = self._recipes_by_cuisine[cuisine]
        nb_total_recipes = len(res)

        if offset:
            res = res[offset:]
        if nb_results:
            res = res[:nb_results]

        return res, nb_total_recipes

    def update_recipe(self, recipe_id: int, data: dict) -> Recipe:
        """
        Updates a recipe.

        :param recipe_id: recipe's id to update
        :param data: dictionary of updated data
        :return: updated Recipe
        """
        data = deepcopy(data)
        data['updated_at'] = datetime.utcnow()

        recipe = self.get_recipe(recipe_id)
        for key, value in data.items():
            recipe.__setattr__(key, value)

        return recipe
