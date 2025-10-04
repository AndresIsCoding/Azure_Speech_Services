import os
from dotenv import load_dotenv
from datetime import datetime
import azure.cognitiveservices.speech as speechsdk

output_dir = "audios"
os.makedirs(output_dir, exist_ok=True)

# Cargar las variables desde .env
load_dotenv()
speech_key = os.getenv("AZURE_SPEECH_KEY")
service_region = os.getenv("AZURE_SPEECH_REGION")

speech_config = speechsdk.SpeechConfig(subscription=speech_key,region=service_region)
audio_input = speechsdk.audio.AudioConfig(use_default_microphone=True)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

