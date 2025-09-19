from sqlmodel import SQLModel, Field

class Url(SQLModel, table=True):
    id: int = Field(
        default=None,
        primary_key=True,
        title="ID",
        description="Indentificador auto-incrementável que dá identidade a registros no banco de dados.")
    url: str = Field(
        title="URL original",
        description="URL para onde a API redirecionará.")
    nick_url: str = Field(
        unique=True,
        title="URL encurtada",
        description="URL que será passada no path e enviará o usuário para a URL original.")