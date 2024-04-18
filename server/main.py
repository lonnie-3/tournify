from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import all_routes
from db.database import Database
app = FastAPI()
db = Database()

@app.on_event("startup")
async def startup():
    await db.create_all()

CORSMiddleware(
    app,
    allow_origins=["http://localhost:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)

app.include_router(all_routes.router)

@app.get("/")
def index():
    return {"message": "Hello World"}

