import boto3
from fastapi import UploadFile, HTTPException, status
from typing import IO, List
import io

from promy_api.infra.env import settings
from promy_api.infra.custom_type import FileType


def get_s3obj():
    return boto3.client(
        's3', aws_access_key_id=settings.aws_access_key_id, aws_secret_access_key=settings.aws_secret_access_key
    )


def get_s3url(key: str) -> str:
    return f"https://{settings.s3_bucket}.s3.{settings.s3_region}.amazonaws.com/{key}"


def upload_image(file: UploadFile, file_type: FileType, id: int) -> str:
    upload_key = f"{file_type}/{id}.{file.filename.split('.')[-1]}"
    s3 = get_s3obj()
    try:
        s3.upload_fileobj(file.file, Bucket=settings.s3_bucket, Key=upload_key, ExtraArgs={'ACL': 'public-read'})
        return get_s3url(upload_key)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"S3에 업로드하는데 실패했습니다")


def delete_image(file_type: FileType, file_name: str) -> None:
    s3 = get_s3obj()
    try:
        s3.delete_object(Bucket=settings.s3_bucket, Key=f"{file_type}/{file_name}")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"S3 오브젝트를 삭제하는데 실패했습니다")
