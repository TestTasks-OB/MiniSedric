from fastapi import APIRouter

from api.routes.interaction import router as interactions_router
from api.routes.upload_file_to_s3 import router as upload_file_to_s3

router = APIRouter()
router.include_router(interactions_router) 
router.include_router(upload_file_to_s3) 