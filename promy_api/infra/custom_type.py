from enum import Enum


class OfferType(str, Enum):
    sangi = "sangi"
    junyeon = "junyeon"


class FileType(str, Enum):
    company_icon = "company_icon"
