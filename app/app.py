from fastapi import FastAPI , HTTPException
from schema import PostCreate
from db import Post , create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from db import create_db_and_tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
app = FastAPI(lifespan=lifespan)


text_posts = {
    1: {"title": "First Post", "content": "Welcome to our journey — the adventure begins now!"},
    2: {"title": "Second Post", "content": "Today is all about taking bold steps toward greatness."},
    3: {"title": "Third Post", "content": "Small wins stack up big — celebrate every move."},
    4: {"title": "Fourth Post", "content": "Life rewards the brave — step into your spotlight."},
    5: {"title": "Fifth Post", "content": "Your dreams are closer than they appear — keep pushing."},
    6: {"title": "Sixth Post", "content": "Create something today your future self will thank you for."},
    7: {"title": "Seventh Post", "content": "Momentum beats perfection — start and adjust later."},
    8: {"title": "Eighth Post", "content": "You don’t need permission to shine — just do it."},
    9: {"title": "Ninth Post", "content": "Every challenge is a chance to reinvent yourself."},
    10: {"title": "Tenth Post", "content": "Stay hungry, stay curious — that’s how legends grow."},
    11: {"title": "Eleventh Post", "content": "The best stories aren’t told. They’re lived."},
    12: {"title": "Twelfth Post", "content": "You’re one decision away from a completely different life."},
    13: {"title": "Thirteenth Post", "content": "Impossible only means no one has done it yet."},
    14: {"title": "Fourteenth Post", "content": "Great things take time — but greatness takes guts."},
    15: {"title": "Fifteenth Post", "content": "Progress is addictive — fuel the obsession."},
    16: {"title": "Sixteenth Post", "content": "Dream loud. Build bold. Execute quietly."},
    17: {"title": "Seventeenth Post", "content": "You don’t rise by waiting — you rise by daring."},
    18: {"title": "Eighteenth Post", "content": "Your potential is a weapon — learn how to use it."},
    19: {"title": "Nineteenth Post", "content": "If it scares you, it’s probably worth doing."},
    20: {"title": "Twentieth Post", "content": "Today’s effort is tomorrow’s legacy — keep moving."}
}


@app.get("/posts")
def all_posts(limit:int=20):
    if limit:
        return (list(text_posts.items()))[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Shut the fuck up")
    return text_posts.get(id)


@app.post("/posts")
def create_post(post : PostCreate):
    new_post = {"title" : post.title , "content" : post.content}
    text_posts[max(text_posts.keys())+1]=new_post
    return new_post