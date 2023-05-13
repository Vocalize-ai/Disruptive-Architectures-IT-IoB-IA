from pocketsphinx import LiveSpeech

for frase in LiveSpeech():
    print("Você falou... ", frase)