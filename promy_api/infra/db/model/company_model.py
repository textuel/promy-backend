from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from promy_api.infra.db.base import Base


class CompanyModel(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    icon = Column(String, nullable=True, default=None)

    offers = relationship("OfferModel", back_populates="company")
