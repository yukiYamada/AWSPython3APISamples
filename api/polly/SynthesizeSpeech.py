from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir


def execute(profile_name="default"):
    """
    execute polly api Synthesize_speech.
    
    Returns
    -----------------------------------
    audioStream(bytes)
    """
    session = Session(profile_name=profile_name)   
    polly = session.client("polly")
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
