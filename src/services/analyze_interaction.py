import boto3 
import asyncio
import uuid
from loguru import logger
import requests
from api.models.InteractionAnalyzerRequest  import InteractionAnalyzerRequestModel
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from api.models.InsigntsModel import InsigntsModel
from typing import List

transcribe_client = boto3.client('transcribe') 

async def get_transcription_job_status(job_name):
    loop = asyncio.get_event_loop()
    while True: 
        status = await loop.run_in_executor(None, lambda: transcribe_client.get_transcription_job(TranscriptionJobName=job_name))
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            return status
        await asyncio.sleep(5)   



async def analyze_interaction(data:InteractionAnalyzerRequestModel)->List[InsigntsModel]:
    (interaction_url, trackers) = (data.interaction_url, data.trackers)
    job_name = f"TranscriptionJobMiniSedric_{uuid.uuid4()}" 
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': interaction_url},
        MediaFormat='mp3',
        LanguageCode='en-US'
    ) 
    status = await get_transcription_job_status(job_name) 
    logger.info(status)
    transcript_file_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']  
    logger.info(transcript_file_uri)
    response = requests.get(transcript_file_uri)
    transcript_data = response.json()
    logger.info(transcript_data)
    transcript_text = transcript_data['results']['transcripts'][0]['transcript']
    logger.info(transcript_text)
    insights = []
    sentences = sent_tokenize(transcript_text) 
    for i, sentence in enumerate(sentences): 
        words = word_tokenize(sentence) 
        for tracker in trackers:
            if tracker in words:
                start_word_index = words.index(tracker)  
                end_word_index = start_word_index + len(tracker.split())   
                insight= InsigntsModel(
                                            sentence_index=i
                                        ,   start_word_index=start_word_index
                                        ,   end_word_index=end_word_index
                                        ,   tracker_value=tracker
                                        ,   transcribe_value=sentence) 
                insights.append(insight)
    logger.info(insights)
    return insights 

