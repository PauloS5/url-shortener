from sqlmodel import SQLModel, Field

class Url(SQLModel, table=True):
    id: int = Field(
        default=None,
        primary_key=True,
        title="Identificador Único",
        description="Indentificador auto-incrementável que dá identidade a registros no banco de dados.")
    original_url: str = Field(
        title="URL original",
        description="URL para onde a API redirecionará.")
    shorted_url: str = Field(
        unique=True,
        title="URL encurtada",
        description="URL que aponntará para a original.")