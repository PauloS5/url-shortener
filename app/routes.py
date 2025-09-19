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
async def register_url(session: Session = Depends(get_session), url_to_register: UrlCreate = Body(embed=True, title="URL", description="URL que será cadastrada no banco de dados")):
    endpoint_nickurl = generate_random_string()

    while findByNick(session, endpoint_nickurl) != None:
        endpoint_nickurl = generate_random_string()
        
    save(session, newurl=url_to_register.url, nickurl=endpoint_nickurl)

@router.put("/url/", response_model=None)
async def update_url(session: Session = Depends(get_session), url_to_update: UrlUpdate = Body(embed=True, title="Nova URL", description="URL que substituirá a antiga")) -> any:
    statement = select(Url).where(Url.id == url_to_update.id)
    result = session.exec(statement)
    if (result):
        url = result.first()
        url.url = url_to_update.url
        session.commit(url)

@router.delete("/url/", response_model=None)
async def delete_url(session: Session = Depends(get_url), url_to_delete: UrlDelete = Body(embed=True)) -> any:
    statement = select(Url).where(Url.id == url_to_delete.id)
    result = session.exec(statement)
    if result:
        url = result.first()
        session.delete(url)
        session.commit()