from sqlmodel import Session, select
from .models import Url

def all(engine) -> list[Url]:
    with Session(engine) as session:
        statement = select(Url)
        results = session.exec(statement)
        return results.all()

def find(engine, id: int) -> Url:
    with Session(engine) as session:
        statement = select(Url).where(Url.id == id).limit(1)
        results = session.exec(statement)
        return results.first()

def findByUrl(engine, url: str) -> Url:
    with Session(engine) as session:
        statement = select(Url).where(Url.nick_url == url).limit(1)
        results = session.exec(statement)
        return results.first()

def save(engine, url: str, nickurl: str) -> None:
    with Session(engine) as session:
        newurl = Url(original_url=url, nick_url=nickurl)
        session.add(newurl)
        session.commit()

def update(engine, id: int, newurl: str) -> None:
    with Session(engine) as session:
        statement = select(Url).where(Url.id == id)
        result = session.exec(statement)
        url = result.first()

        if (url):
            url.original_url = newurl
            session.add(url)
            session.commit()

def delete(engine, id: int) -> None:
    with Session(engine) as session: