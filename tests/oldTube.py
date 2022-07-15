import os
from pytube import YouTube

#* La funcion descargara el video y ordenara segun los datos que reciba la function como argumentos

def execDownload(video_link, itag_selector_video, video_path):
    if os.path.isfile(video_path):
        print("Error, la ruta donde se vaya a guardar la descarga debe de ser una carpeta y has elegido un fichero!")
    elif os.path.isdir(video_path):
        print("la descarga comenzara ahora...")
        try:
            finalSelection = video_link.streams.get_by_itag(itag_selector_video)
            finalSelection.download(video_path)
        except:
            print("No se ha podido descargar el archivo, ¿has introducido bien la URL?")

        #* Descargamos el video y verificamos que el archivo se encuentre en su ubicacion
        final_name = finalSelection.download(video_path)        
        test_file = os.path.exists(final_name)
        if test_file == True:
            print("La carpeta es valida y el archivo ya ha sido descargado!")
        else:
            print("Algo a ido mal, revisa que hayas introducido bien los datos")

#* Instrucciones imperativas
user_link = input("Inserta aqui el enlace del video: ")
video_to_download = YouTube(user_link)
user_format_video = input("Quieres descargar solo audio?: [S]i o [N]o: ") #* Tipos de descarga

#* Limpiamos la consola y recogemos las opciones
os.system("clear")
print("Que calidad en Kbps deberia de tener su descarga?\n")
#* Validamos el tipo de descarga y mostramos por pantalla las distintas descargas disponibles
if "S" in user_format_video or "s" in user_format_video:
    for i in video_to_download.streams.filter(only_audio = True):
        print(i)
elif "N" in user_format_video or "n" in user_format_video:
    for i in video_to_download.streams:
        print(i)

user_download_video = input("\nSeleccione el video por el identificador 'itag' en la que encontrara los Kbps: ")
print("\n")

#* Volvemos a limpiar la consola y pedimos que se nos introduzca una ruta

os.system("clear")
print("A continuacion introduce una ruta (puede ser absoluta o relativa) donde vayas a descargar el archivo\nTen en cuenta que si la ruta es relativa\nEsta se tomara en cuenta desde la ruta de ejecucion del archivo")
user_path = input("Introduce una ruta: ")

execDownload(video_to_download, user_download_video, user_path)