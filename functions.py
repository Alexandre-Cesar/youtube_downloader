import os
from pathlib import Path
import subprocess
import tkinter as tk
from PIL import Image, ImageTk

def baixar_audio(url, tipo, label):
    diretorio_saida='/output'
    home = str(Path.home())
    diretorio_saida = os.path.join(home, 'Downloads')
    try:
        if tipo == 'video':
            comando = f'yt-dlp -f bestvideo+bestaudio -o "{diretorio_saida}\\Musicas\%(title)s.mp4" {url}'

        if tipo == 'audio': 
            comando = f"yt-dlp --extract-audio --audio-format mp3 -o {diretorio_saida}\\Musicas\\%(title)s.%(ext)s {url}"

        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        if resultado.returncode == 0:
            
            texto = "Download concluido"
        else:
            texto = "Não foi possivel realizar download"  
        
        label.config(text=f"{texto}")
    except:

        label.config(text=f"Não foi possivel realizar download")
        


def on_enter(e):
    # Escurecendo o botão ao passar o mouse
    e.widget.config(bg="#0d730d")  
    
def on_leave(e):
    # Voltando à cor original
    e.widget.config(bg="#0a5c0a")
    