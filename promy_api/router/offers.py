from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from promy_api.infra.db.base import get_db
from promy_api.dto.offer_dto import OfferOutputDTO, OfferInputDTO, OfferBaseDTO
from promy_api.util.offer_util import OfferUtil

router = APIRouter()


@router.get("/", response_model=List[OfferOutputDTO])
async def get_offers(db: Session = Depends(get_db)):
    return OfferUtil.get_offers(db)


@router.get("/{offer_id}", response_model=OfferOutputDTO)
async def get_offer_by_id(offer_id: int, db: Session = Depends(get_db)):
    db_offer = OfferUtil.get_offer_by_id(db, offer_id)
    if db_offer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="요청한 공고 아이디가 존재하지 않습니다.")
    return db_offer


@router.post("/", response_model=OfferOutputDTO, status_code=status.HTTP_201_CREATED)
async def create_offer(dto: OfferInputDTO, db: Session = Depends(get_db)):
    return OfferUtil.create_offer(db, dto)


@router.put("/{offer_id}", response_model=OfferOutputDTO)
async def update_offer(offer_id: int, dto: OfferBaseDTO, db: Session = Depends(get_db)):
    db_offer = OfferUtil.get_offer_by_id(db, offer_id)
    if db_offer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="요청한 공고 아이디가 존재하지 않습니다.")
    return OfferUtil.fix_offer(db, db_offer, dto)


@router.delete("/{offer_id}")
async def delete_offer(offer_id: int, db: Session = Depends(get_db)):
    db_offer = OfferUtil.get_offer_by_id(db, offer_id)
    if db_offer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="요청한 공고 아이디가 존재하지 않습니다.")
    OfferUtil.delete_offer(db, db_offer)
    return {"status": "success"}
