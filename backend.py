from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"status": "Backend running"}


def is_url(text: str) -> bool:
    # basic domain / url detection
    url_regex = re.compile(
        r'^(https?:\/\/)?'      # http:// or https:// (optional)
        r'([\w\-]+\.)+'         # domain
        r'[a-zA-Z]{2,}'         # TLD
        r'(\/.*)?$'             # path (optional)
    )
    return bool(url_regex.match(text))


@app.get("/search")
def search(q: str = Query(...)):
    q = q.strip()

    # If user typed a URL
    if is_url(q):
        if not q.startswith("http"):
            q = "https://" + q
        return RedirectResponse(url=q)

    # Otherwise, do Google search
    google_url = f"https://www.google.com/search?q={q}"
    return RedirectResponse(url=google_url)


@app.get("/lucky")
def lucky(q: str = Query(...)):
    lucky_url = f"https://www.google.com/search?q={q}&btnI=I"
    return RedirectResponse(url=lucky_url)
