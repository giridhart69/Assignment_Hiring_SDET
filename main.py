from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def find_longest_substring(inp: str):
    s = inp.lower()
    a = 0
    b = 0
    c = set()
    longest_substring = ""
    for i in range(len(s)):
        while s[i] in c:
            c.remove(s[a])
            a += 1
        c.add(s[i])
        if len(c) > b:
            b = len(c)
            longest_substring = s[a:i+1]
    return b, longest_substring

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process", response_class=HTMLResponse)
async def process_input(request: Request, input_text: str = Form(...)):
    length, substring = find_longest_substring(input_text)
    return templates.TemplateResponse("output.html", {"request": request, "length": length, "substring": substring})


@app.post("/test-process")
async def process_input(request_body: dict):
    inptstr = request_body.get("inptstr")
    length, substring = find_longest_substring(inptstr)
    return dict(Length=length,Substring=substring)

@app.get("/output", response_class=HTMLResponse)
async def read_output(request: Request):
    response = templates.TemplateResponse("output.html", {"request": request, "length": None, "substring": None})
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, post-check=0, pre-check=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response