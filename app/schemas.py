from sqlmodel import SQLModel, Field

class UrlBase(SQLModel):
    pass

class UrlCreate(UrlBase):
    pass

class UrlRead(UrlBase):
    pass

class UrlUpdate(UrlBase):
    pass

class UrlDelete(UrlBase):
    pass