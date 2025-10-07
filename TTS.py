import os
from dotenv import load_dotenv
from datetime import datetime
import azure.cognitiveservices.speech as speechsdk


def TTS(text: str, voz_femenina):
    output_dir = "audios"
    os.makedirs(output_dir, exist_ok=True)

    # Cargar las variables desde .env
    load_dotenv()
    speech_key = os.getenv("AZURE_SPEECH_KEY")
    service_region = os.getenv("AZURE_SPEECH_REGION")

    # Configurar el servicio de habla
    speech_config = speechsdk.SpeechConfig(subscription=speech_key,
                                           region=service_region)
    voz = "es-CO-SalomeNeural" if voz_femenina else "es-CO-GonzaloNeural"
    speech_config.speech_synthesis_voice_name = voz
    # Configurar la salida de audio
    audio_config = speechsdk.audio.AudioOutputConfig(
        filename=os.path.join(output_dir, f"salida_TTS.wav"))
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,
                                              audio_config=audio_config)

    synthesizer.speak_text_async(text).get()


