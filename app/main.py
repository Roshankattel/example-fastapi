
from fastapi import FastAPI
import uvicorn
from . import models
from .database import engine
from .routers import users, posts, auth, vote
from fastapi.middleware.cors import CORSMiddleware


# As Alembic is defined to update the db
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# origin defines list of domains that can talk with the API

# origins = [
#     "http://www.google.com",
#     "https://www.youtube.com",
# ]


origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],            # defines allowed methods like PUT, POST
    allow_headers=["*"],            # defines list of headers alloweded by API
)

# we can also use of regex using
# allow_origin_regex= 'https://.*\.example\.org'


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

# if __name__ == "__main__":
#     uvicorn.run(app,port=8000, debug=True)
