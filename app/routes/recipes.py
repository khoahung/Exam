from fastapi import APIRouter
import pandas as pd
import os


router = APIRouter()

@router.get("/")
def get_recipes():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, '..', '..', 'ingredients.csv')
    csv_path = os.path.abspath(csv_path)
    df = pd.read_csv(csv_path, encoding='utf-8')
    print(df.head()) 
    print("sdfsdfsdfsdfsd") 
    #total_cost = sum(ingredient.cost_per_gram * quantity for ingredient, quantity in ingredients)
    return {"message": "Hello from FastAPI!"}


@router.get("/{id}/")
def get_recipesByID():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, '..', '..', 'ingredients.csv')
    csv_path = os.path.abspath(csv_path)
    df = pd.read_csv(csv_path, encoding='utf-8')
    print(df.head()) 
    print("sdfsdfsdfsdfsd") 
    #total_cost = sum(ingredient.cost_per_gram * quantity for ingredient, quantity in ingredients)
    return {"message": "Hello from FastAPI!"}

