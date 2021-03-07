from fastapi import UploadFile
from sqlalchemy.orm import Session
from typing import List

from promy_api.infra.db.model.company_model import CompanyModel
from promy_api.dto.company_dto import CompanyBaseDTO
from promy_api.infra.s3.base import upload_image, delete_image
from promy_api.infra.custom_type import FileType


class CompanyUtil:
    @classmethod
    def get_companies(cls, db: Session) -> List[CompanyModel]:
        return db.query(CompanyModel).all()

    @classmethod
    def get_company_by_id(cls, db: Session, company_id: int):
        return db.query(CompanyModel).filter(CompanyModel.company_id == company_id).first()

    @classmethod
    def create_company(cls, db: Session, dto: CompanyBaseDTO) -> CompanyModel:
        db_company = CompanyModel(name=dto.name)
        db.add(db_company)
        db.commit()
        db.refresh(db_company)
        return db_company

    @classmethod
    def update_company_icon(cls, db: Session, db_company: CompanyModel, file: UploadFile) -> CompanyModel:
        if db_company.icon:
            delete_image(FileType.company_icon, db_company.icon.split('/')[-1])
        db_company.icon = upload_image(file, FileType.company_icon, db_company.company_id)
        db.commit()
        return db_company

    @classmethod
    def fix_company(cls, db: Session, db_company: CompanyModel, dto: CompanyBaseDTO) -> CompanyModel:
        db_company.name = dto.name
        db.commit()
        return db_company

    @classmethod
    def delete_company(cls, db: Session, db_company: CompanyModel):
        db.delete(db_company)
        db.commit()
