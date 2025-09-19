from sqlmodel import SQLModel, Field

class UrlBase(SQLModel):
    url: str = Field(
        title="URL original",
        description="URL na quala API redirecionará.",
        max_length=511)

class UrlCreate(UrlBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "url": "https://example.com"
                }
            ]
        }
    }

class UrlRead(UrlBase):
    id: int = Field(
        title="ID",
        description="Indentificador único da URL a ser buscada.")
    nick_url: str = Field(
        title="URL de apelido",
        description="End-point que apontará para a URL relacionada.")
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "url": "https://example.com",
                    "id": "1",
                    "nick_url": "ex"
                }
            ]
        }
    }

class UrlUpdate(UrlBase):
    id: int = Field(
        title="ID",
        description="Identificador único que aponta para o registro a ser atualizado.")
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "url": "https://example.com",
                    "id": 10
                }
            ]
        }
    }

class UrlDelete(UrlBase):
    id: int = Field(
        title="ID",
        description="Identificador único que aponta para o registro a ser excluído.")
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "url": "https://example.com",
                    "id": 1
                }
            ]
        }
    }