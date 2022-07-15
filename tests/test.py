from os import path

from pytube import YouTube

x = YouTube("https://www.youtube.com/watch?v=wvz97-lNPH8")

#print(path.join(path.dirname(__file__)), "/../logs/response.txt")

diccionario = {
    "hola": "lol",
    "Recontra": "lol"
}

print(str(diccionario))