from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

class PlayerBase(BaseModel):
    name: str

class PlayerCreate(PlayerBase):
    pass

class PlayerOut(PlayerBase):
    id: int
    user_name:str
    
    class Config:
        orm_mode = True

class PlayersOut(PlayerBase):
    id:int

class LeagueBase(BaseModel):
    name: str

class LeagueCreate(LeagueBase):
    pass

class LeagueOut(LeagueBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class GameBase(BaseModel):
    league_id: int
    user_id1: int
    user_id2: int

class GameCreate(GameBase):
    pass

class GameOut(GameBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class PlayerStatsBase(BaseModel):
    game_id: int
    player_id: int
    goals_scored: int
    assists: int

class PlayerStatsCreate(PlayerStatsBase):
    pass

class PlayerStatsOut(PlayerStatsBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserStatsBase(BaseModel):
    league_id: int
    wins: int
    draws: int
    losses: int
    goals_scored_for: int
    goals_scored_against: int
    points: int

class UserStatsUpdate(UserStatsBase):
    wins: Optional[int] = None
    draws: Optional[int] = None
    losses: Optional[int] = None
    goals_scored_for: Optional[int] = None
    goals_scored_against: Optional[int] = None
    points: Optional[int] = None

class UserStatsCreate(UserStatsBase):
    pass

class UserStatsOut(UserStatsBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
