from gtts import gTTS
from playsound import playsound
import os
#C:/Users/logonrmlocal/Desktop/agenda.txt

myPath = input("Digite o local do arquivo: ")
teste = os.path.isfile(myPath)

if teste:
    with open(myPath, 'r', encoding='utf-8') as file:
        print("loading file")
        texto = file.read()
        print("Reading text")
        print(texto)
        audio = gTTS(texto, lang='pt')
        audio.save('agenda.mp3')
        playsound("agenda.mp3")

else:
    print("caminho inválido! tiauuu")