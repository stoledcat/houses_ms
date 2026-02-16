from sqlmodel import Field, SQLModel


class House(SQLModel, table=True):
    __tablename__ = "houses"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str = Field(default="")
    price: int = Field(default=0, index=True)
    active: bool = Field(default=True, index=True)