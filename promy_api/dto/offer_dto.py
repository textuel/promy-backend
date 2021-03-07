from pydantic import BaseModel
from datetime import date
from typing import Optional

from promy_api.infra.custom_type import OfferType
from promy_api.dto.company_dto import CompanyInfoDTO


class OfferBaseDTO(BaseModel):
    job: str
    description: str
    link: str
    end_date: Optional[date]
    kind: OfferType

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "job": "백엔드 개발자 (경력)",
                "description": "나와 우리의 성장을 돕는 서비스. 그리고 나에게 필요한 서비스를 함께 만들어 가실 새로운 팀원을 기다립니다. 서핏에 관심 있으신 분이라",
                "link": "https://wanted.com/...",
                "end_date": date.today(),
                "kind": OfferType.sangi
            }
        }


class OfferInputDTO(OfferBaseDTO):
    company_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                **(OfferBaseDTO.Config.schema_extra["example"]),
                "company_id": 1
            }
        }


class OfferOutputDTO(OfferBaseDTO):
    offer_id: int
    company: CompanyInfoDTO

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                **(OfferBaseDTO.Config.schema_extra["example"]),
                "offer_id": 1,
                "company": CompanyInfoDTO.Config.schema_extra["example"]
            }
        }

