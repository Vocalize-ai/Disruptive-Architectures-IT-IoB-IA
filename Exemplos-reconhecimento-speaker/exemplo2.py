import speech_recognition as sr

reconhecedor = sr.Recognizer()

#NECESSÁRIO O PIP INSTALL PYAUDIO

microphone = sr.Microphone()
while True:
    try:
        with microphone as mic:

            reconhecedor.adjust_for_ambient_noise(mic)
            print("Fala tu menó....")
            audio = reconhecedor.listen(mic)
            print("Reconhecendo...")

            texto = reconhecedor.recognize_google(audio, language='pt')
            print(texto)
    except:
        print("Bugou, nem sei...")

    