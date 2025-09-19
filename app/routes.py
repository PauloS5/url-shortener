from fastapi import APIRouter, Path, Body, Depends
from sqlmodel import Session

from .database import get_session
from .crud import *
from .schemas import *
from .helpers import *

router = APIRouter()

@router.get("/url/", response_model=list[UrlRead])
async def list_all_urls(session: Session = Depends(get_session)) -> any:
    return all_urls(session)

@router.get("/url/{id}", response_model=UrlRead|None)
async def get_url(session: Session = Depends(get_session), id: int = Path(title="Identificador Único", description="ID que seráusado para buscar uma url")) -> any:
    return find_url(session, id)

@router.post("/url/", response_model=None)
async def register_url(session: Session = Depends(get_session), url_to_register: UrlCreate = Body(embed=True, title="URL", description="URL que será cadastrada no banco de dados")):
    endpoint_nickurl = generate_random_string()

    while find_url_by_nick(session, endpoint_nickurl) != None:
        endpoint_nickurl = generate_random_string()
        
    save_url(session, newurl=url_to_register.url, nickurl=endpoint_nickurl)

@router.put("/url/", response_model=None)
async def update_url(session: Session = Depends(get_session), url_to_update: UrlUpdate = Body(embed=True, title="Nova URL", description="URL que substituirá a antiga")) -> any:
    update_url(session, url_to_update.id, url_to_update.url)

@router.delete("/url/{id}", response_model=None)    
async def delete_url(session: Session = Depends(get_session), id: int = Path(title="Identificador Único", description="ID do elemento que será excluído")) -> any:
    delete_url(session, id)