from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os, logging
import aiofiles
from helpers.config import GetSettings, Settings
from models import ResponseSignal
from controllers import DataController, ProjectController
logger=logging.getLogger('uvicorn.error')
data_router=APIRouter(
    prefix="/api/data",
    tags=["api","data"],
)

@data_router.post("/upload/{project_id}")

async def upload(project_id: str,file: UploadFile, app_settings: Settings=Depends(GetSettings)):
    data_controller=DataController()
    is_valid, result_signal=data_controller.ValidateFile(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=400,
            content= {
                "signal": result_signal
            }
        )
    project_dir_path=ProjectController().get_project_path(project_id=project_id)
    file_path, file_id= data_controller.generate_unique_filepath(orig_file_name= file.filename, project_id=project_id)

    try:
        async with aiofiles.open(file_path,"wb") as f:
            while chunk :=await file.read(app_settings.File_Default_Chunk_Size):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error while uploading file: {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content= {
                "signal": ResponseSignal.File_Uploaded_Fail.value
                }
            )


    return JSONResponse(
            content= {
                "signal": ResponseSignal.File_Uploaded_Success.value,
                "file_id": file_id
            }
        )