from fastapi import APIRouter, Depends, status, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from typing import List
import re

from promy_api.infra.db.base import get_db
from promy_api.dto.company_dto import CompanyBaseDTO, CompanyInfoDTO
from promy_api.util.company_util import CompanyUtil

router = APIRouter()


@router.get("/", response_model=List[CompanyInfoDTO])
async def get_companies(db: Session = Depends(get_db)):
    return CompanyUtil.get_companies(db)


@router.get("/{company_id}", response_model=CompanyInfoDTO)
async def get_company_by_id(company_id: int, db: Session = Depends(get_db)):
    db_company = CompanyUtil.get_company_by_id(db, company_id)
    if db_company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="요청한 회사 아이디가 존재하지 않습니다.")
    return db_company


@router.post("/", response_model=CompanyInfoDTO, status_code=status.HTTP_201_CREATED)
async def create_company(dto: CompanyBaseDTO, db: Session = Depends(get_db)):
    return CompanyUtil.create_company(db, dto)


@router.put("/{company_id}/icon", response_model=CompanyInfoDTO, status_code=status.HTTP_201_CREATED)
async def update_company_icon(company_id: int, icon: UploadFile = File(...), db: Session = Depends(get_db)):
    if not re.match('image/', icon.content_type):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="이미지 파일만 등록 가능합니다")
    db_company = CompanyUtil.get_company_by_id(db, company_id)
    if db_company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="요청한 회사 아이디가 존재하지 않습니다.")
    return CompanyUtil.update_company_icon(db, db_company, icon)


@router.put("/{company_id}", response_model=CompanyInfoDTO)
async def fix_company(company_id: int, dto: CompanyBaseDTO, db: Session = Depends(get_db)):
    db_company = CompanyUtil.get_company_by_id(db, company_id)
    if db_company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="요청한 회사 아이디가 존재하지 않습니다.")
    return CompanyUtil.fix_company(db, db_company, dto)


@router.delete("/{company_id}")
async def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = CompanyUtil.get_company_by_id(db, company_id)
    if db_company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="요청한 회사 아이디가 존재하지 않습니다.")
    CompanyUtil.delete_company(db, db_company)
    return {"status": "success"}
