import speech_recognition as sr

reconhecedor = sr.Recognizer()
microfone = sr.Microphone()

with microfone as mic:

    reconhecedor.adjust_for_ambient_noise(mic)
    while True:
        try:

            print("Fale o que deseja calcular: ")
            audio = reconhecedor.listen(mic)
            print("Aguarde...")
            conta = reconhecedor.recognize_google(audio, language='pt')
            v1 = conta.split(' ')[0]
            operador = conta.split(' ')[1]
            v2 = conta.split(' ')[2]

            if operador == "+":
                print(f'a soma entre {v1} + {v2} deu {v1+v2}')
            elif operador == "-":
                print(f'a soma entre {v1} - {v2} deu {v1-v2}')
            elif operador == "x":
                print(f'a soma entre {v1} * {v2} deu {v1*v2}')
            elif operador == "/" and v2!= 0:
                print(f'a soma entre {v1} / {v2} deu {v1/v2}')

        except:
            print("Deu ruim amigão")