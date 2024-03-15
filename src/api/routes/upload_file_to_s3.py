from fastapi import File, UploadFile, APIRouter, Depends, HTTPException
from core.settings.app import AppSettings
from core.config import get_app_settings
from api.models.UploadResponseModel import UploadResponseModel
from api.models.ErrorResponseModel import ErrorResponseModel
import boto3
import os
  
s3_client = boto3.client('s3')


router = APIRouter(
    tags=['audio']
) 

@router.post("/audio/upload"
             , summary="put file to s3"   
             , responses={
                    200: {"model": UploadResponseModel, "description": "Successful upload mp3 file"},            
                    400: {"model": ErrorResponseModel,"description": "Bad Request"},
                    500: {"model": ErrorResponseModel,"description": "Internal Server Error"}
            }
)
async def upload_file_to_s3(
                            file: UploadFile = File(...)
                        ,   settings: AppSettings = Depends(get_app_settings)):
    """
        put file to s3
    """   
    if not file.filename.endswith('.mp3'):
        return {"error": "File format is not MP3"}
    try: 
        file_content = await file.read()  
        response = s3_client.put_object(
            Bucket=settings.BUCKET_NAME,
            Key=file.filename,
            Body=file_content
        )
        
        s3_uri = f"s3://{settings.BUCKET_NAME}/{file.filename}" 
        return UploadResponseModel( message="File uploaded successfully",s3_uri=s3_uri,response=response)  
    except Exception as e:
        raise HTTPException(status_code=500, detail=ErrorResponseModel(
            error_code=500,
            error_message=str(e)
        )) 
