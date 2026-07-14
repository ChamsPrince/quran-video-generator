from fastapi import APIRouter
from services.data_service import DataService

router = APIRouter()

data_service = DataService()


@router.get("/surahs")
def get_surahs():
    return data_service.get_surahs()


@router.get("/surahs/{number}")
def get_surah(number: int):
    return data_service.get_surah(number)