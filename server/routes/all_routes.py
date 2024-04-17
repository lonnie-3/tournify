from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(
    prefix="/api",
    tags=["Api"],
)


@router.get("/")
def create_user():
    return {"api routes ok"}