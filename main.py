import pytube
import os


def audio_dowloader():
    link = str(input("Digite o link do video que deseja baixar: \n"))
    yt = pytube.YouTube(link)
    stream = yt.streams.get_audio_only()
    audio = stream.download("/home/eduardo/Vídeos")

    base, ext = os.path.splitext(audio)
    new_file = base + '.mp3'
    os.rename(audio, new_file)

def video_dowloader():
    link = str(input("Digite o link do video que deseja baixar: \n"))
    yt = pytube.YouTube(link)
    video = yt.streams.get_highest_resolution()
    video.download("/home/eduardo/Vídeos")

print("1- Baixar video ou 2- Baixar Somente o audio\n")
escolha = int(input("digite o numero da função que deseja realizar: \n"))

if (escolha == 1):
    video_dowloader()

else:
    audio_dowloader()