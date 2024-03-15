from fastapi import APIRouter,Depends, HTTPException
from loguru import logger 

from api.models.InteractionAnalyzerRequest  import InteractionAnalyzerRequestModel
from api.models.InteractionAnalyzerResponse import InteractionAnalyzerResponseModel 
from api.models.ErrorResponseModel import ErrorResponseModel
from core.settings.app import AppSettings
from core.config import get_app_settings
from services.analyze_interaction import analyze_interaction 
router = APIRouter(
    tags=['audio']
)
import traceback

@router.post("/audio/interaction_url"
             , summary="analyze human interactions"   
             , responses={
                    200: {"model": InteractionAnalyzerResponseModel, "description": "Successful analyze of audio interactions"},               
                    400: {"model": ErrorResponseModel,"description": "Bad Request"},
                    500: {"model": ErrorResponseModel,"description": "Internal Server Error"}
            }
)
async def interaction_url(
                            input_data: InteractionAnalyzerRequestModel
                        ,   settings: AppSettings = Depends(get_app_settings)):
    """
        analyze human interactions
    """   

    try:
        result = await analyze_interaction(input_data)
        logger.info(result)
        response = InteractionAnalyzerResponseModel(insignts=result)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=ErrorResponseModel(
            error_code=500,
            error_message=str(e)
        )) 
