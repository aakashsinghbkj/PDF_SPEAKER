from gtts import gTTS

text = "Hello Guys, what's up?"

language = "en"

obj = gTTS(text = text, Lang= language, slow = False)

obj.save("sample.mp3")