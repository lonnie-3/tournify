from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now()) 

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now()) 

class League(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    league_id = Column(Integer, ForeignKey("leagues.id"), nullable=False)
    user_id1 = Column(Integer, ForeignKey("users.id"), nullable=False)
    user_id2 = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.now())

class PlayerStats(Base):
    __tablename__ = "player_stats"

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    goals_scored = Column(Integer, nullable=False)
    assists = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())

class UserStats(Base):
    __tablename__ = "user_stats"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    league_id = Column(Integer, ForeignKey("leagues.id"), nullable=False)
    wins = Column(Integer, nullable=False)
    draws = Column(Integer, nullable=False)
    losses = Column(Integer, nullable=False)
    goals_scored_for = Column(Integer, nullable=False)
    goals_scored_against = Column(Integer, nullable=False)
    points = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())