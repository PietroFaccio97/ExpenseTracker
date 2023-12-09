from io import BytesIO

import pandas as pd
from fastapi import APIRouter, UploadFile

from src.api.responses.SuccessResponse import SuccessResponse

router = APIRouter(
    prefix="/files",
    tags=["files"],
    default_response_class = SuccessResponse
)


@router.post("/xlsx")
def post_report(file: UploadFile):
    data = file.file.read()
    df = pd.read_excel(BytesIO(data), engine = "openpyxl", decimal = ",")
    return SuccessResponse(message = "File uploaded successfully")
