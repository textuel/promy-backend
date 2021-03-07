from pydantic import BaseModel
from typing import Optional


class CompanyBaseDTO(BaseModel):
    name: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Classting",
            }
        }


class CompanyInfoDTO(CompanyBaseDTO):
    icon: Optional[str]
    company_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                **(CompanyBaseDTO.Config.schema_extra["example"]),
                "icon": "https://s3.~~~",
                "company_id": 1,
            }
        }
