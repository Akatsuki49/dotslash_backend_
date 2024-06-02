import os
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    SpeakOptions,
)

def tts1(resp):
    load_dotenv()
    SPEAK_OPTIONS = {"text": resp}
    filename = "output.wav"
    deepgram = DeepgramClient(api_key='8cc6a875400724ceb8d69acd65bf7fa17279fef2')
    options = SpeakOptions(
        model="aura-orpheus-en",
        encoding="linear16",
        container="wav"
    )
    speech = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
    

