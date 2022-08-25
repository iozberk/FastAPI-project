from fastapi import FastAPI
from .import models
from .database import engine
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse 
from .routers import post, user, auth, vote

app = FastAPI()

origins =["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# models.Base.metadata.create_all(bind=engine)
@app.get("/")
def root():
    return FileResponse('index.html')

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)