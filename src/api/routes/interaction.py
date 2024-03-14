from fastapi import APIRouter,Depends 
from loguru import logger 

from src.api.models.InteractionAnalyzerRequest  import InteractionAnalyzerRequestModel
from src.api.models.InteractionAnalyzerResponse import InteractionAnalyzerResponseModel
from src.api.models.InsigntsModel import InsigntsModel
from src.core.settings.app import AppSettings
from src.core.config import get_app_settings
router = APIRouter(
    tags=['audio']
)
import traceback

@router.post("/audio/interaction_url"
             , summary="analyze human interactions"   
             , responses={
                    200: {"model": InteractionAnalyzerResponseModel, "description": "Successful analyze of audio interactions"}
            }
)
async def interaction_url(
                            input_data: InteractionAnalyzerRequestModel
                        ,   settings: AppSettings = Depends(get_app_settings)):
    """
         Change password for the user by his request 
    """  
    row_test = InsigntsModel(sentence_index=1,start_word_index=1,end_word_index=1,tracker_value="hi",transcribe_value="world")
    response = InteractionAnalyzerResponseModel( 
           insignts=[row_test]
        )  
    return response 