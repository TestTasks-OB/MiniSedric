 

from pydantic import BaseModel 
from typing import List
from src.api.models.InsigntsModel import InsigntsModel

class InteractionAnalyzerResponseModel(BaseModel):
    """
    Model for result of analyze audio interactions stored in s3
    """ 
    insignts: List[InsigntsModel]
 