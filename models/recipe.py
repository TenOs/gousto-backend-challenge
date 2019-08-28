from typing import List
from pydantic import BaseModel
from datetime import datetime


class Recipe(BaseModel):
    """
    This class represents a Recipe object.
    """

    # mandatory fields
    id: int
    created_at: datetime
    updated_at: datetime
    box_type: str
    title: str
    slug: str
    marketing_description: str
    calories_kcal: int
    protein_grams: int
    fat_grams: int
    carbs_grams: int
    recipe_diet_type_id: str
    season: str
    protein_source: str
    preparation_time_minutes: int
    shelf_life_days: int
    equipment_needed: str
    origin_country: str
    recipe_cuisine: str
    gousto_reference: int

    # optional fields
    short_title: str = None
    bulletpoint1: str = None
    bulletpoint2: str = None
    bulletpoint3: str = None
    base: str = None
    in_your_box: str = None


class RecipeSummary(BaseModel):
    """
    This class represents a RecipeSummary object.
    """
    id: int
    title: str
    marketing_description: str


class RecipeListResponse(BaseModel):
    """
    This class represents a RecipeListResponse.
    """
    data: List[RecipeSummary]
    total: int
    next_offset: int = None


class RecipeUpdateRequest(BaseModel):
    """
    This class represents a RecipeUpdateRequest.

    All fields are optional, allowing partial updates on a Recipe.
    """
    box_type: str = None
    title: str = None
    slug: str = None
    marketing_description: str = None
    calories_kcal: int = None
    protein_grams: int = None
    fat_grams: int = None
    carbs_grams: int = None
    recipe_diet_type_id: str = None
    season: str = None
    protein_source: str = None
    preparation_time_minutes: int = None
    shelf_life_days: int = None
    equipment_needed: str = None
    origin_country: str = None
    recipe_cuisine: str = None
    gousto_reference: int = None

    short_title: str = None
    bulletpoint1: str = None
    bulletpoint2: str = None
    bulletpoint3: str = None
    base: str = None
    in_your_box: str = None
