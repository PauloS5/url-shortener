from sqlmodel import SQLModel, Field

class UrlBase(SQLModel):
    original_url: str = Field(
        title="URL original",
        description="URL na quala API redirecionará.",
        max_length=511)

class UrlCreate(UrlBase):
    pass

class UrlRead(UrlBase):
    id: int = Field(
        title="ID",
        description="Indenttificador único auto-incrementável")
    nick_url: str = Field(
        default=None,
        title="URL de apelido",
        description="End-point que apontará para a URL relacionada.")

class UrlUpdate(UrlBase):
    id: int = Field(
        title="ID",
        description="Identificador único que aponta para o registro a ser atualizado.")

class UrlDelete(UrlBase):
    id: int = Field(
        title="ID",
        description="Identificador único que aponta para o registro a ser excluído.")