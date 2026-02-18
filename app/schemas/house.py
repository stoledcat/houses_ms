from pydantic import BaseModel, Field


class HouseFullSchema(BaseModel):
    id: int
    name: str = Field(description="Название дома")
    description: str = Field(description="Краткое описание")
    price: int = Field(description="Цена в рублях", examples=["5000", "10000"])
    active: bool



class HouseDetailSchema(BaseModel):
    id: int
    name: str = Field(description="Название дома")
    description: str = Field(description="Краткое описание")
    price: int = Field(description="Цена в рублях", examples=["5000", "10000"])


class HouseItemSchema(BaseModel):
    id: int = Field(description="ID объявления")
    name: str = Field(description="Название дома")
    price: int = Field(description="Цена в рублях", examples=["5000", "10000"])