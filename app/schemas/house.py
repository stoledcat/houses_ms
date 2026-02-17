from pydantic import BaseModel, Field


class HouseFullSchema(BaseModel):
    id: int = Field(description="ID объявления")
    name: str = Field(description="Название")
    description: str = Field(description="Описание")
    price: int = Field(description="Стоимость")
    active: bool = Field(description="Объявление активно")



class HouseDetailSchema(BaseModel):
    id: int = Field(description="ID объявления")
    name: str = Field(description="Название")
    description: str = Field(description="Описание")
    price: int = Field(description="Стоимость")


class HouseItemSchema(BaseModel):
    id: int = Field(description="ID объявления")
    name: str = Field(description="Название")
    price: int = Field(description="Стоимость")