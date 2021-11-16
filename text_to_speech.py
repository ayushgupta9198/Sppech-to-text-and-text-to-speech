from gtts import gTTS
import os

# The text that you want to convert to audio
mytext = 'His abode which you had fixed in a bowery or country seat. Have a short distance from the city. Just at what is now called dutch street. Soon abounded with proofs of his ingenuity. Patent smokejack. It required a horse to work some. Dutch oven roasted meat without fire. Carts that went before the horses. Weather cox that turned against the wind and other wrongheaded contrivances. So just understand confound it all beholders.'

# Language in which you want to convert
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("text_to_speech.mp3")

