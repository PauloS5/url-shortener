from sqlmodel import Session, select
from .models import Url

def all_url(session: Session) -> list[Url]:
    statement = select(Url)
    results = session.exec(statement)
    return results.all()

def find_url(session: Session, id: int) -> Url:
    statement = select(Url).where(Url.id == id).limit(1)
    results = session.exec(statement)
    return results.first()

def find_url_by_nick(session: Session, nick: str) -> Url:
    statement = select(Url).where(Url.nick_url == nick).limit(1)
    results = session.exec(statement)
    return results.first()

def save_url(session: Session, url_data: Url) -> None:
    session.add(url_data)
    session.commit()

def update_url(session: Session, url_data: Url, newurl: str) -> None:
    url_data.url = newurl
    session.add(url_data)
    session.commit()

def delete_url(session: Session, url_data: Url) -> None:
    session.delete(url_data)
    session.commit()