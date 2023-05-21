from GPT_API import API_KEY
import requests
import json

headers = {"Authorization": f'Bearer {API_KEY}'}

link = "https://api.openai.com/v1/models"

req = requests.get(link, headers=headers)
print(req)
print(req.text)

id_modelo = "gpt-3.5-turbo"

body_mensagem = {
  "model":id_modelo,
  "messages": [{"role": "user", "content": f"{userSpeech: await regeneratSpeech(userSpeech)}"}]
}
body_mensagem = json.dumps(body_mensagem)

{
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": "Hello!"}]
}