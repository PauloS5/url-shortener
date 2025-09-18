from fastapi import APIRouter, Path, Depends
from sqlmodel import Session

from .database import get_session
from .crud import all
from .schemas import UrlRead 

router = APIRouter()

@router.get("/url", response_model=list[UrlRead])
async def all_url(session: Session = Depends(get_session)) -> any:
    return all(session)