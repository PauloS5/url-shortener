from fastapi import APIRouter, Path, Depends
from sqlmodel import Session

from .database import get_session
from .crud import *
from .schemas import UrlRead 

router = APIRouter()

@router.get("/url/", response_model=list[UrlRead])
async def list_urls(session: Session = Depends(get_session)) -> any:
    return all(session)

@router.get("/url/{id}", response_model=UrlRead|None)
async def get_url(session: Session = Depends(get_session), id: int = Path(title="Identificador Único", description="ID que seráusado para buscar uma url")):
    url = find(session, id)

    return url

