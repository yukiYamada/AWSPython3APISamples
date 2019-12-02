from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

session = Session(profile_name="user1")
polly = session.client("polly")

try:
    response = polly.synthesize_speech(Text="Hello World!", OutputFormat="mp3", VoiceId="Joanna")

except(BotoCoreError, ClientError) as error:
    print(error)
    sys.exit(-1)

if "AudioStream" in response:
    output = "speech.mp3"
    try:
        #pyton3 not supported file()
        #file.write(stream.read())
        file = open(output, 'wb')
        file.write(response["AudioStream"].read())
    except IOError as error:
        print(error)
        sys.exit(-1)
    finally:
        file.close()
else:
    print("Could not stream audio")
    sys.exit(-1)


