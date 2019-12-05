from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

session = Session(profile_name="user1")
polly = session.client("polly")

def execute():
    """
    execute polly api Synthesize_speech.
    
    Returns
    -----------------------------------
    audioStream(bytes)
    """
    
    try:
        response = polly.synthesize_speech(Text="Hello World!", OutputFormat="mp3", VoiceId="Joanna")

    except(BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)
    
    if "AudioStream" in response:
        return response["AudioStream"]
    
    else:
        print("Could not stream audio")
        sys.exit(-1)
