from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2Templates
templates = Jinja2Templates(directory="templates")


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):  # Request ko argument me lena zaroori hai
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/message", response_class=JSONResponse)
async def message():
    return {"message": "Hello from FastAPI ahmad"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
