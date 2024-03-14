 

from pydantic import BaseModel 
from typing import List

class InteractionAnalyzerRequestModel(BaseModel):
    """
    Model for request to analyze audio interactions stored in s3
    """ 
    interaction_url: str
    trackers: List[str]
 