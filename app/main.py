from fastapi import FastAPI
from .import models
from .database import engine
from starlette.responses import FileResponse 
from .routers import post, user, auth
from .config import settings 

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
@app.get("/")
def root():
    return FileResponse('index.html')

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

