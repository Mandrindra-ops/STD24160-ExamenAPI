from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()

# Q1 :
@app.get("/ping")
def ping():
    return Response(content="pong", media_type="text/plain", status_code=200)

# Q2 :
@app.get("/Home")
def Home(): 
    return Response(content="<h1>Welcome to the Home page</h1>", media_type="text/html", status_code=200)

# Q3 :
@app.exception_handler(404)
def not_found(request, exc):
    return Response(content="<h1>404 NOT FOUND</h1>", media_type="text/html", status_code=404)

# Q4 :
@app.post("/posts")
def create_post(author: str, title: str, content: str, creation_datetime: str):
    post = {
        "author": author,
        "title": title,
        "content": content,
        "creation_datetime": creation_datetime
    }
    return Response(content=str(post), media_type="application/json", status_code=201, details={"ok": True})

# Q5 : 
@app.get("/posts")
def get_posts():
    posts = [
        {"author": "Alice", "title": "First Post", "content": "This is the first post", "creation_datetime": "2023-10-01T12:00:00"},
        {"author": "Bob", "title": "Second Post", "content": "This is the second post", "creation_datetime": "2023-10-02T12:00:00"}
    ]
    return Response(content=str(posts), media_type="application/json", status_code=200, details={"ok": True})

# Q6 :
@app.put("/posts")
def update_post(title: str, author: str, content: str, creation_datetime: str):
    post = {
        "author": author,
        "title": title,
        "content": content,
        "creation_datetime": creation_datetime
    }
    return Response(content=str(post), media_type="application/json", status_code=200, details={"ok": True})

