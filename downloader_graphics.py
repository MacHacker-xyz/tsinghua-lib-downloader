import os
import tkinter as tk
from tkinter.constants import NO
import tkinter.font as tkFont
from tkinter import filedialog
import downloader
import threading
from PIL import Image,ImageTk

thread = None


def begin():
    url = entry1.get()
    quality = str(scale2.get())
    download_path = filedialog.askdirectory()
    if len(download_path)==0:
        return
    var1.set("初始化！")
    window.update()
    global thread
    thread = threading.Thread(target=downloader.implicit_download,args=(url, quality, download_path, window, var1))
    thread.start()

if __name__=="__main__":
    window = tk.Tk()
    window.geometry("650x391")
    window.title("教参平台爬虫")
    window.maxsize(width=650,height=391)
    window.minsize(width=650,height=391)
    
    ft = tkFont.Font(family='ComicSansMS', size=20, weight=tkFont.BOLD)
    
    var1 = tk.StringVar()
    label1 = tk.Label(
        window,
        text="网址",
        font=ft,
    )
    label1.place(
        anchor="n",
        x=325,
        y=0
    )
    entry1 = tk.Entry(
        window,
        font=ft,
    )
    entry1.place(
        anchor="n",
        x=325,
        y=40
    )
    label2 = tk.Label(
        window,
        text="质量（1-96）",
        font=ft,
    )
    
    label2.place(
        anchor="n",
        x=325,
        y=80
    )
    scale2 = tk.Scale(
        window,
        from_=1,
        to=96,
        length=300,
        variable=96,
        font=ft,
        orient=tk.HORIZONTAL,
    )
    scale2.set(96)
    scale2.place(
        anchor="n",
        x=325,
        y=120
    )
    label_warning = tk.Label(
        window,
        text="本软件仅供学习编程知识\n发售盗版内容者承担一切法律责任",
        font=tkFont.Font(family='ComicSansMS', size=20, weight=tkFont.BOLD),
        fg="Red",
    )
    label_warning.place(
        anchor="n",
        x=325,
        y=170
    )
    button = tk.Button(
        window,
        text='下载',
        command=begin,
        font=tkFont.Font(family='ComicSansMS', size=30, weight=tkFont.BOLD),
        height=1,
        width=5,
    )
    
    button.place(
        anchor="n",
        x=325,
        y=250
    )
    label3 = tk.Label(
        window,
        textvariable=var1,
        font=ft,
    )
    label3.place(
        anchor="n",
        x=325,
        y=300
    )
    window.mainloop()