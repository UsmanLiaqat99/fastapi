from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/about")
def about():
    return {"message": "About Page"}


# -----    Blogs  ---
@app.get("/blogs", tags=["blog"])
def blogs(limit=10, published: bool = True):
    if published:
        return {"message": f"{limit} published blogs"}
    else:
        return {"message": f"{limit} blogs"}


@app.get("/blog/{id}", tags=["blog"])
def blog(id: int):
    return {"message": id}


@app.get("/blog/{id}/comments", tags=["blog"])
def comments(id):
    return {"message": {"1", "2"}}


@app.get("/blog/{id}/comments/{comment_id}", tags=["blog"])
def comment(id, comment_id):
    return {"message": {"1", "2"}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog", tags=["blog"])
def create_blog(request: Blog):
    return {"message": "Blog is Created"}
