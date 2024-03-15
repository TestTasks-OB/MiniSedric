from pydantic import BaseModel, Field

class UploadResponseModel(BaseModel):
    message: str = Field(..., description="A message about the upload status")
    s3_uri: str = Field(..., description="The S3 URI of the uploaded file")
    response: dict = Field(..., description="The original response from the S3 upload operation")