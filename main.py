import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pytube import YouTube
from pytube.exceptions import *
from tkinter import *

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x450")
root.resizable(False, False)
root.configure(background="#c65975")

def download_video():
    url = urlEntry.get()
    folder = folderEntry.get()
    format_choice = format.get()

    if not url:
        messagebox.showerror("Помилка!", "Будь ласка, вставьте URL-посилання!")
        return
    if not folder:
        messagebox.showerror("Помилка!", "Будь ласка, вкажіть шлях файлу!")
        return

    try:
        yt = YouTube(url, use_oauth=True)
        print(yt.streams.filter(only_audio=True).desc())
        if format_choice == "Video Max. res.":
            stream = yt.streams.get_highest_resolution()
            filename = stream.default_filename.split(".")
            stream.download(folder, filename=filename[0] + " Max Resolution." + filename[1])
            messagebox.showinfo("Успіх", "Відео успішно завантажено! Знаходиться в теці - " + folder)
        elif format_choice == "Audio Max. res.":
            stream2 = yt.streams.filter(only_audio=True).desc().first()
            filename = stream2.default_filename.split(".")
            stream2.download(folder, filename=filename[0] + " Max Resolution.mp3")
            messagebox.showinfo("Успіх", "Аудіо успішно завантажено! Знаходиться в теці - " + folder)
        else:
            match format_choice:
                case "Video AVI":
                    stream3 = yt.streams.get_highest_resolution()
                    filename = stream3.default_filename.split(".")
                    stream3.download(folder, filename=filename[0] + ".avi")
                    messagebox.showinfo("Успіх", "Відео успішно завантажено! Знаходиться в теці - " + folder)
                case "Video MKV":
                    stream4 = yt.streams.get_highest_resolution()
                    filename = stream4.default_filename.split(".")
                    stream4.download(folder, filename =filename[0] + " .mkv")
                    messagebox.showinfo("Успіх", "Відео успішно завантажено! Знаходиться в теці - " + folder)
                case "Video MOV":
                    stream5 = yt.streams.get_highest_resolution()
                    filename = stream5.default_filename.split(".")
                    stream5.download(folder, filename = filename[0] + ".mov")
                    messagebox.showinfo("Успіх", "Відео успішно завантажено! Знаходиться в теці - " + folder)
                case "Audio OGG":
                    stream6 = yt.streams.filter(only_audio=True).desc().first()
                    filename = stream6.default_filename.split(".")
                    stream6.download(folder, filename=filename[0] + "-audio.ogg")
                    messagebox.showinfo("Успіх", "Аудіо успішно завантажено! Знаходиться в теці - " + folder)
                case "Audio WAV":
                    stream6 = yt.streams.filter(only_audio=True).desc().first()
                    filename = stream6.default_filename.split(".")
                    stream6.download(folder, filename=filename[0] + "-audio.wav")
                    messagebox.showinfo("Успіх", "Аудіо успішно завантажено! Знаходиться в теці - " + folder)
                case "Audio APE":
                    stream6 = yt.streams.filter(only_audio=True).desc().first()
                    filename = stream6.default_filename.split(".")
                    stream6.download(folder, filename=filename[0] + "-audio.ape")
                    messagebox.showinfo("Успіх", "Аудіо успішно завантажено! Знаходиться в теці - " + folder)
                case _:
                    print("Case def")
    except VideoPrivate:
        messagebox.showerror("Помилка!", "Відео приватне.")
    except VideoRegionBlocked:
        messagebox.showerror("Помилка!", "Недоступне завантаження, причина - регіон.")
    except LiveStreamError:
        messagebox.showerror("Помилка!", "Відео являється прямою трансялцією.")
    except Exception as e:
        messagebox.showerror("Помилка!", "Некоректне посилання! Неможливо завантажити файл.")
        print(e)
        print(e.__class__)

def select_folder():
    folder_selected = filedialog.askdirectory()
    folderEntry.delete(0, tk.END)
    folderEntry.insert(0, folder_selected)

labelStyle = ttk.Style()
labelStyle.configure("CustomStyle.TLabel",background = "#5975c6", padding = 7, foreground = "white")

urlLabel = ttk.Label(root, text="YouTube URL:", style="CustomStyle.TLabel")
urlLabel.pack(pady=10)

entryStyle = ttk.Style()
entryStyle.configure("CustomStyle.TEntry", foreground="red", padding=5)

buttonStyle = ttk.Style()
buttonStyle.configure("CustomStyle.TButton", background="#5975c6", foreground="black", padding=5, relief="solid")

urlEntry = ttk.Entry(root, width=50, style="CustomStyle.TEntry")
urlEntry.pack(pady=5)

folderLabel = ttk.Label(root, text="Select Folder:", style="CustomStyle.TLabel")
folderLabel.pack(pady=10)

folderEntry = ttk.Entry(root, width=50, style="CustomStyle.TEntry")
folderEntry.pack(pady=5)

folderButton = ttk.Button(root, text="Browse", command=select_folder, style="CustomStyle.TButton")
folderButton.pack(pady=5)

formatLabel = ttk.Label(root, text="Select Format:", style="CustomStyle.TLabel")
formatLabel.pack(pady=10)

format = StringVar(value="Video Max. res.")
formatBox = ttk.Combobox(root, textvariable=format, values=["Video Max. res.", "Video AVI", "Video MKV", "Video MOV",
                                                            "Audio Max. res.", "Audio OGG", "Audio WAV", "Audio APE"])
formatBox.pack(pady=5)

downloadButton = ttk.Button(root, text="Download", command=download_video, style="CustomStyle.TButton")
downloadButton.pack(pady=20)

root.mainloop()