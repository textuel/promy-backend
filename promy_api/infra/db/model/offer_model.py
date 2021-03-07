from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship

from promy_api.infra.db.base import Base
from promy_api.infra.custom_type import OfferType


class OfferModel(Base):
    __tablename__ = "offers"

    offer_id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.company_id"))
    job = Column(String)
    description = Column(String)
    link = Column(String)
    end_date = Column(Date, nullable=True, default=None)
    kind = Column(Enum(OfferType))

    company = relationship("CompanyModel", back_populates="offers", uselist=False)
