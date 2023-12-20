from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import crud, schema
from app.dependencies import get_db

router: APIRouter = APIRouter(
    prefix="/challenges", dependencies=[Depends(get_db)]
)


@router.get("", response_model=list[schema.Challenge])
def get_challenges(db: Session = Depends(get_db)):
    challenges = crud.get_challenges(db)
    return challenges


@router.get("/{day_id}", response_model=schema.Challenge)
def get_challenge(day_id: str, db: Session = Depends(get_db)):
    challenge = crud.get_challenge_by_day_id(db, day_id)
    return challenge
