from sqlmodel import SQLModel, Field

class UrlBase(SQLModel):
    original_url: str = Field(max_length=511)

class UrlCreate(UrlBase):
    pass

class UrlRead(UrlBase):
    id: int = Field()
    nick_url: str = Field(default=None)

class UrlUpdate(UrlBase):
    id: int

class UrlDelete(UrlBase):
    id: int = Field()