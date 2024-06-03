from sqlalchemy.orm import Session
import models, schemas

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password  # For simplicity, not hashing password here
    db_user = models.User(username=user.username, password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_match(db: Session, match: schemas.MatchCreate):
    db_match = models.Match(title=match.title, schedule=match.schedule, details=match.details)
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match

def get_matches(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Match).offset(skip).limit(limit).all()

def get_match(db: Session, match_id: int):
    return db.query(models.Match).filter(models.Match.id == match_id).first()

def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()

def add_team_member(db: Session, team_id: int, name: str, stats: str):
    db_player = models.Player(name=name, stats=stats, team_id=team_id)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_player_stats(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()
