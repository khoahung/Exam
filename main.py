
from fastapi import FastAPI
from app.routes import ingredient
from app.routes import recipes
# Initialize FastAPI application
# This file is the entry point for the FastAPI application.



app = FastAPI()

app.include_router(recipes.router, prefix="/recipes")
app.include_router(ingredient.router, prefix="/ingredient")




