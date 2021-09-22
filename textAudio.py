from gtts import gTTS
from playsound import playsound

audio = 'talk.mp3'
language = 'en'
sp = gTTS(text="enter yuor text which you want to convert into audio file",
          lang=language, slow=False)
sp.save(audio)
playsound(audio)
