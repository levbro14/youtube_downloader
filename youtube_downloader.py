import tkinter as tk
from tkinter import PhotoImage, ttk, filedialog, messagebox
from pytube import YouTube
import threading
from PIL import ImageTk, Image
import pathlib, os.path

root = tk.Tk()
root.geometry("500x500")
root.resizable(False, False)
root.title("YouTube downloader")

appdir = pathlib.Path(__file__).parent.resolve()
root.iconbitmap(os.path.join(appdir,'icon.ico'))

directory = ""
def file():
    global directory
    directory = filedialog.askdirectory()
    if directory != "":
        lbl_location.config(text=directory)
    else:
        messagebox.showerror("Ошибка", "Выберите местоположение")

def download_video():
    entry_url.config(state="disabled")
    path_btn.config(state="disabled")
    down_btn.config(state="disabled")
    try:
        url = entry_url.get()
        if len(url) >= 5:
            if directory != "Местоположение":
                yt = YouTube(url)
                stream = yt.streams.get_highest_resolution()
                stream.download(output_path=directory)
                messagebox.showinfo("Успешно", f"Видео: {stream.title} скачано успешно в {directory}")
                entry_url.config(state="normal")
                path_btn.config(state="normal")
                down_btn.config(state="normal")
            else:
                messagebox.showerror("Ошибка", "Выберите местоположение")
                entry_url.config(state="normal")
                path_btn.config(state="normal")
                down_btn.config(state="normal")
        else:
            messagebox.showerror("Ошибка", "Введите ссылку")
            entry_url.config(state="normal")
            path_btn.config(state="normal")
            down_btn.config(state="normal")
    except Exception as ex:
        messagebox.showerror("Ошибка", ex)
        entry_url.config(state="normal")
        path_btn.config(state="normal")
        down_btn.config(state="normal")

image = Image.open(os.path.join(appdir,'icon.png')).resize((80, 80))
logo = ImageTk.PhotoImage(image)
ttk.Label(text="YouTube downloader", image=logo, compound="left", font=("Arial bold", 25)).place(x=80, y=15)
ttk.Label(text="Ссылка на видео: ", font=("Arial bold", 16)).place(x=250, y=130, anchor="center")
entry_url = ttk.Entry(width=70)
entry_url.place(x=250, y=170, anchor="center", height=25)
path_btn = ttk.Button(text="Выберите местоположение видео", command=file)
path_btn.place(x=135, y=210, anchor="center")
lbl_location = ttk.Label(text="Местоположение", font=("Arial bold", 16))
lbl_location.place(x=250, y=200)
down_btn = ttk.Button(text="Скачать", command=lambda: threading.Thread(target=download_video).start())
down_btn.place(x=250, y=320, anchor="center")


root.mainloop()

