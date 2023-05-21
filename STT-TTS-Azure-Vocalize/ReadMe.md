First to test install virtual enviroment and all librarys

python -m venv venv 
#certify to activate the "./venv/Scripts/Activate.ps1"
python -m pip install --upgrade pip

# Text to Speech and Speech to Text
pip install azure-cognitiveservices-speech

# Api chat-GPT
pip install openai
pip install requests
pip install fuzzywuzzy