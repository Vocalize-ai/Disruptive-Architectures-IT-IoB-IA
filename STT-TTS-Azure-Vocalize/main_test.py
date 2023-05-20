import requests
import json
import azure.cognitiveservices.speech as speech
from API import SPEECH_KEY
from API import SERVICE_REGION
from API import ENDPOINT

# Configurar o ambiente azure
speech_config = speech.SpeechConfig(subscription = SPEECH_KEY, region=SERVICE_REGION)


# Definir o idioma e a voz para português
speech_config.speech_synthesis_language = 'pt-BR'
# Iniciar o reconhecimento de fala a partir do microfone
speech_recognizer = speech.SpeechRecognizer(speech_config=speech_config, language='pt-BR')

print("Comece a falar...")
userSpeech = speech_recognizer.recognize_once()

# Configurar a mensagem de texto para síntese de fala
text_to_speak = "Olá! Seja bem vindo"
n_entendi = "Nenhum texto reconhecido."

# Iniciar a síntese de fala
speech_synthesizer = speech.SpeechSynthesizer(speech_config=speech_config)


# Salvar o áudio gerado em um arquivo
output_file = "output.wav"

print(f"Áudio salvo em: {output_file}")

# Exibir o texto transcrito
if userSpeech.reason == speech.ResultReason.RecognizedSpeech:
    if userSpeech.text == 'Olá, lazer.':
        resultSpeech = speech_synthesizer.speak_text(text_to_speak)
    else:
        resultSpeech = speech_synthesizer.speak_text(userSpeech.text)
        print("Texto transcrito:", userSpeech.text)

elif userSpeech.reason == speech.ResultReason.NoMatch:
    resultSpeech = speech_synthesizer.speak_text(n_entendi)
elif userSpeech.reason == speech.ResultReason.Canceled:
    print("Reconhecimento de fala cancelado:", userSpeech.cancellation_details.reason)



