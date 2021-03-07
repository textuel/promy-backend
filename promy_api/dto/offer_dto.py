from pydantic import BaseModel
from datetime import date


class OfferBaseDTO(BaseModel):
    company_id: int
