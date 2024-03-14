 

from pydantic import BaseModel 
from typing import List


class InsigntsModel(BaseModel):
    """
    Model for row of insignt result 
    """ 
    sentence_index: int
    start_word_index: int
    end_word_index: int
    tracker_value: str
    transcribe_value: str
 