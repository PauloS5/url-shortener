from fastapi import APIRouter, Path, Body, Depends
from sqlmodel import Session

from .database import get_session
from .crud import *
from .schemas import *
from .helpers import *

router = APIRouter()

@router.get("/url/", response_model=list[UrlRead])
async def list_urls(session: Session = Depends(get_session)) -> any:
    return all(session)

@router.get("/url/{id}", response_model=UrlRead|None)
async def get_url(session: Session = Depends(get_session), id: int = Path(title="Identificador Único", description="ID que seráusado para buscar uma url")) -> any:
    return find(session, id)

@router.post("/url/", response_model=None)
async def register_url(session: Session = Depends(get_session), newurl: UrlCreate = Body(embed=True, title="URL", description="URL que será cadastrada no banco de dados")):
    endpoint_nickurl = generate_random_string()

    while findByNick(endpoint_nickurl) != None:
        endpoint_nickurl = generate_random_string()
        
    save(session, url=newurl.original_url, nickurl=endpoint_nickurl)

@router.put("/url/", response_model=None)
async def update_url(session: Session = Depends(get_session), newurl: UrlUpdate = Body(embed=True, title="Nova URL", description="URL que substituirá a antiga")) -> any:
    statement = select(Url).where(Url.id == newurl.id)
    result = session.exec(statement)
    if (result):
        url = result.first()
        url.url = newurl.url
        session.commit(url)