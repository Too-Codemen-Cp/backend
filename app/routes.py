import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from werkzeug.utils import secure_filename

from .helpers import recognize_static

router = APIRouter()

UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))

@router.get("/{file_path:path}", response_class=FileResponse)
async def get_static_file(file_path: str) -> FileResponse:
    file_location = os.path.join(UPLOAD_FOLDER, file_path)
    if not os.path.isfile(file_location):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_location)

@router.post("/file")
async def upload_file(file: UploadFile = File(...)) -> JSONResponse:
    try:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        result = recognize_static(filename)
        return JSONResponse(content={"result": result}, status_code=200)

    except Exception as ex:
        return JSONResponse(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "result": "false",
                "error_type": str(type(ex)),
                "error_message": str(ex),
            },
        )
