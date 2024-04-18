from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import Database
from db.dbfunncs import get_db
from models.models import Player, User
from models.schemas import PlayerCreate, PlayerOut, UserCreate, UserOut

router = APIRouter(
    prefix="/api",
    tags=["Api"],
)
database = Database()

@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_data = User(name=user.name)
    db_user = db.query(User).filter(User.name == user_data.name).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

    db.add(user_data)
    db.commit()
    db.refresh(user_data)  

    return user_data


@router.post("/user/{id}/players", status_code=status.HTTP_201_CREATED, response_model=PlayerOut)
async def add_player(player: PlayerCreate, id: int, db: Session = Depends(get_db)):
    check_user = db.query(User).filter(User.id == id).first()
    if not check_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    username = check_user.name
    player_data = Player(name=player.name, user_name=username)  
    db.add(player_data)
    db.commit()
    db.refresh(player_data)  

    return player_data

@router.get("/user/{id}/players", response_model=list[PlayerOut])
def get_players(db: Session = Depends(get_db)):
    players = db.query(Player).filter(Player.user_name == id).all()
    return players