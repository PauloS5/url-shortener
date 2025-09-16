from sqlmodel import Session
from .models import Url

def all(session: Session) -> any:
    return

def find(session: Session, id: int) -> any:
    return

def findByUrl(session: Session, url: str) -> any:
    return

def save(session: Session, url: str, nickurl) -> any:
    new = Url(original_url=url, nick_url=nickurl)
    session.add(new)
    session.commit()

def update(session: Session, id: int, newurl: str) -> any:
    return

def delete(session: Session, id: int):
    return