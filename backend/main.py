from fastapi import FastAPI
from endpoints import photos
from endpoints import users


app = FastAPI()
app.include_router(photos.router)
app.include_router(users.router)