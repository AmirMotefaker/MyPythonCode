# Code by amotef@gmail.com

# Language Translator Using Google API

# import googletrans
 
# print(googletrans.LANGUAGES)

from googletrans import Translator

translator = Translator()

result = translator.translate('ich liebe dich')

print(result.src)
print(result.dest)
print(result.origin)
print(result.text)
print(result.pronunciation)
