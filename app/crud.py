from sqlmodel import Session, select
from .models import Url

def all(session: Session) -> list[Url]:
    statement = select(Url)
    results = session.exec(statement)
    return results.all()

def find(session: Session, id: int) -> Url:
    return

def findByUrl(session: Session, url: str) -> Url:
    return

def save(session: Session, url: str, nickurl) -> None:
    newurl = Url(original_url=url, nick_url=nickurl)
    session.add(newurl)
    session.commit()

def update(session: Session, id: int, newurl: str) -> None:
    return

def delete(session: Session, id: int) -> None:
    return