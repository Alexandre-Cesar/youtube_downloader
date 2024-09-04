from functions import *

import tkinter as tk
def enviar_link_musica():
    link = entry.get()

    print("Link enviado:", link)
    texto = 'Carregando'
    load.config(text=texto)
    load.grid(row=4, column=1, sticky="nsew")
    root.after(0, baixar_audio, link, 'audio', load)

def enviar_link_video():
    link = entry.get()

    print("Link enviado:", link)
    texto = 'Carregando'
    load.config(text=texto)
    load.grid(row=4, column=1, sticky="nsew")
    root.after(0, baixar_audio, link, 'video', load)


    
root = tk.Tk()
#root.geometry("675x200")
root['bg'] = '#333333'

icon_path = "play_button_icon.ico"

#icon = Image.open(icon_path)
#photo = ImageTk.PhotoImage(icon)
#root.iconphoto(False, photo)


label = tk.Label(root, background= "#333333", fg='white', text="Digite o link:",font='Calibri 17 bold')
load = tk.Label(root, background= "#333333", fg='white', font='Calibri 17 bold')

frame1 = tk.Frame(root, width=100, height=200)

#caixa
entry = tk.Entry(root)
entry.config(width='70')

#Baixar audio
button = tk.Button(frame1, text="Baixar audio", command=enviar_link_musica,
                   fg="white", 
                   bg="#333333",  
                   font='Calibri 17 bold',
                   borderwidth=2,  
                   relief=tk.FLAT  
                   )
button.config(background= "#0a5c0a", fg='white',border= 3)

#baixar video
button_v = tk.Button(frame1, text="Baixar video", command=enviar_link_video,
                   fg="white", 
                   bg="#333333",  
                   font='Calibri 17 bold',
                   borderwidth=2, 
                   relief=tk.FLAT ) 
button_v.config(background= "#0a5c0a", fg='white',border= 3)

for b in (button, button_v):
    b.bind("<Enter>", on_enter)
    b.bind("<Leave>", on_leave)

label.grid(row=0, column=0, sticky='w')
entry.grid(row=2, column=1, sticky="w")
frame1.grid(row=3, column=1, sticky='n')
button.grid(row=0, column=0, sticky="s")
button_v.grid(row=0, column=5, sticky="nsew")
load.grid(row=4, column=1, sticky="nsew")

root.mainloop()