import speech_recognition as sr
import os

microfone = sr.Microphone()
reconhecedor = sr.Recognizer()

with microfone as mic:
    
    reconhecedor.adjust_for_ambient_noise(mic)
    print("Deseja abrir sua agenda: ")
    audio = reconhecedor.listen(mic)
    print("Aguarde, reconhecendo comando...")
    texto = reconhecedor.recognize_google(audio, language='pt').upper()
    lista = ['SIM', 'OK', 'OKAY', 'AHAM']
    if texto in lista:
        print("Ok, abrindo arquivo...")
        os.system('agenda.txt')
    else:
        print("nem queria mesmo bobão...")
    