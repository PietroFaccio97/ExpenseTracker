from fastapi.responses import JSONResponse


class SuccessResponse(JSONResponse):
    def __init__(self, message: str, status_code: int = 200):
        super().__init__(content={
            "message": message
        }, status_code=status_code)
