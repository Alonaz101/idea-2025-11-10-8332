from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Mood-based Recipe Recommendation API")

# In-memory database substitutes
recipes_db = [
    {"id": 1, "name": "Spaghetti Carbonara", "mood": "happy"},
    {"id": 2, "name": "Tomato Soup", "mood": "sad"},
]

class Recipe(BaseModel):
    id: int
    name: str
    mood: str

class MoodInput(BaseModel):
    mood: str

@app.get("/recipes", response_model=List[Recipe])
def get_recipes():
    return recipes_db

@app.get("/recipe/{recipe_id}", response_model=Recipe)
def get_recipe(recipe_id: int):
    for recipe in recipes_db:
        if recipe["id"] == recipe_id:
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.post("/mood")
def post_mood(mood_input: MoodInput):
    # Simple filter by mood
    matching = [r for r in recipes_db if r["mood"] == mood_input.mood]
    return matching

@app.get("/health")
def health_check():
    return {"status": "ok"}
