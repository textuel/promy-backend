from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List

from promy_api.infra.db.model.offer_model import OfferModel
from promy_api.dto.offer_dto import OfferInputDTO, OfferBaseDTO


class OfferUtil:
    @classmethod
    def get_offers(cls, db: Session) -> List[OfferModel]:
        return db.query(OfferModel).order_by(desc(OfferModel.offer_id)).all()

    @classmethod
    def get_offer_by_id(cls, db: Session, offer_id: int):
        return db.query(OfferModel).filter(OfferModel.offer_id == offer_id).first()

    @classmethod
    def create_offer(cls, db: Session, dto: OfferInputDTO) -> OfferModel:
        db_offer = OfferModel(
            company_id=dto.company_id,
            job=dto.job,
            description=dto.description,
            link=dto.link,
            end_date=dto.end_date,
            kind=dto.kind
        )
        db.add(db_offer)
        db.commit()
        db.refresh(db_offer)
        return db_offer

    @classmethod
    def fix_offer(cls, db: Session, db_offer: OfferModel, dto: OfferBaseDTO) -> OfferModel:
        db_offer.job = dto.job
        db_offer.description = dto.description
        db_offer.link = dto.link
        db_offer.end_date = dto.end_date
        db_offer.kind = dto.kind
        db.commit()
        return db_offer

    @classmethod
    def delete_offer(cls, db: Session, db_offer: OfferModel):
        db.delete(db_offer)
        db.commit()
