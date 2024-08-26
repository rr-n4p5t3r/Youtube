import subprocess

def descargar_video(url):
    try:
        command = ["yt-dlp", "-f", "bestvideo+bestaudio", "--merge-output-format", "mp4", url]
        subprocess.run(command, check=True)
        print("Descarga de video completada")
    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un error: {e}")

def descargar_audio(url):
    try:
        command = ["yt-dlp", "-f", "bestaudio", "--extract-audio", "--audio-format", "mp3", url]
        subprocess.run(command, check=True)
        print("Descarga de audio completada")
    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    url = input("Ingrese la URL del video de YouTube: ")
    opcion = input("¿Desea descargar el video (mp4) o solo el audio (mp3)? (video/audio): ").strip().lower()

    if opcion == "video":
        descargar_video(url)
    elif opcion == "audio":
        descargar_audio(url)
    else:
        print("Opción no válida. Por favor, elija 'video' o 'audio'.")
