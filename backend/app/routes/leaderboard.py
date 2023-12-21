from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import crud, schema
from app.dependencies import get_db

router: APIRouter = APIRouter(
    prefix="/leaderboard", dependencies=[Depends(get_db)]
)


@router.get("", response_model=list[schema.Leaderboard])
def get_leaderboard(db: Session = Depends(get_db)):
    leaderboard = crud.get_leaderboard(db)
    return leaderboard
