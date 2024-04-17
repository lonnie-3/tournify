from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import all_routes
app = FastAPI()

CORSMiddleware(app, allow_origins=["http://localhost:5172"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(all_routes.router)

@app.get("/")
def index():
    return {"message": "Hello World"}

