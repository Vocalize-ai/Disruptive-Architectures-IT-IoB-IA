import requests
import json
import azure.cognitiveservices.speech as speech
import asyncio
from fuzzywuzzy import fuzz

from API import SPEECH_KEY, SERVICE_REGION
from GPT_API import API_KEY

# Configurando parâmetros de requisição do chatGPT
headers = {"Authorization": f'Bearer {API_KEY}', "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo-0301"

# Configurar o ambiente Azure
speech_config = speech.SpeechConfig(subscription=SPEECH_KEY, region=SERVICE_REGION)

# Iniciar o reconhecimento de fala a partir do microfone
speech_recognizer = speech.SpeechRecognizer(speech_config=speech_config, language='pt-BR')

# Definir o idioma e a voz para português
speech_config.speech_synthesis_language = 'pt-BR'

# Iniciar a síntese de fala
speech_synthesizer = speech.SpeechSynthesizer(speech_config=speech_config)


# Função para a Lizer dizer um texto como parâmetro
def LizerSay(txt):
    return speech_synthesizer.speak_text(txt)


async def main():
    print("Inicialize a Lizer!")
    userSpeech = speech_recognizer.recognize_once()

    # Configurar a mensagem de texto para síntese de fala
    welcome = "Olá! Seja bem-vindo. Em que posso te ajudar?"
    n_entendi = "Nenhum texto reconhecido."

    palavra = 'OK, LAZER.'
    texto = userSpeech.text.upper()

    if userSpeech.reason == speech.ResultReason.RecognizedSpeech and fuzz.ratio(palavra, texto) >= 80:
        LizerSay(welcome)
        
        userSpeech = await regeneratSpeech(userSpeech)
        body_mensagem = {
            "model": id_modelo,
            "messages": [{"role": "user", "content": userSpeech.text}]
        }
        body_mensagem = json.dumps(body_mensagem)
        req = requests.post(link, headers=headers, data=body_mensagem)
        resp = req.json()
        message = resp["choices"][0]["message"]["content"]
        print(message)
        LizerSay(message)

    elif userSpeech.reason == speech.ResultReason.NoMatch:
        LizerSay(n_entendi)
    elif userSpeech.reason == speech.ResultReason.Canceled:
        print("Reconhecimento de fala cancelado:", userSpeech.cancellation_details.reason)


async def regeneratSpeech(userSpeech):
    userSpeech = speech_recognizer.recognize_once()
    return userSpeech


# Executa o loop de eventos assíncronos
asyncio.run(main())
