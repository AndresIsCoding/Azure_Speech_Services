import os
from dotenv import load_dotenv
from datetime import datetime
import azure.cognitiveservices.speech as speechsdk


def TTS(text: str):
    output_dir = "audios"
    os.makedirs(output_dir, exist_ok=True)

    # Cargar las variables desde .env
    load_dotenv()
    speech_key = os.getenv("AZURE_SPEECH_KEY")
    service_region = os.getenv("AZURE_SPEECH_REGION")

    # Configurar el servicio de habla
    speech_config = speechsdk.SpeechConfig(subscription=speech_key,
                                           region=service_region)
    speech_config.speech_synthesis_voice_name = "es-CO-GonzaloNeural"

    # Configurar la salida de audio
    timestamp = datetime.now().strftime("%d_%m_%Y_%H%M%S")
    audio_config = speechsdk.audio.AudioOutputConfig(
        filename=os.path.join(output_dir, f"salida_TTS.wav"))
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,
                                              audio_config=audio_config)

    synthesizer.speak_text_async(text).get()
