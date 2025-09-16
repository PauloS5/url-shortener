from sqlmodel import Session
from .models import Url

def all(session: Session) -> list[Url]:
    return

def find(session: Session, id: int) -> Url:
    return

def findByUrl(session: Session, url: str) -> Url:
    return

def save(session: Session, url: str, nickurl) -> None:
    new = Url(original_url=url, nick_url=nickurl)
    session.add(new)
    session.commit()

def update(session: Session, id: int, newurl: str) -> None:
    return

def delete(session: Session, id: int) -> None:
    return