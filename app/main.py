# from lib2to3.pytree import Base
# from msilib.schema import Error
# from numbers import Real
# from telnetlib import STATUS

# from xmlrpc.client import boolean

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from FastApi.app.routers.vote import vote
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
    
# Home page
@app.get("/")
def root():
    return {"message": "Hello World!"}









# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="#1Adrian", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Succesful Connection')
#         break
#     except Exception as error:
#         print('Connection failed', error)
#         time.sleep(2)


