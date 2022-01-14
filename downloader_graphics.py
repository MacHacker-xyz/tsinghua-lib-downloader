import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import downloader
import threading

try:
    from PIL import Image,ImageTk
except:
    import os
    os.system('sudo pip3 install PIL')
    from PIL import Image,ImageTk


def begin():
    url = entry1.get()
    pdf_name = entry2.get()
    download_path = filedialog.askdirectory()
    
    if len(download_path)==0 :
        var1.set("请输入完整")
        return
    
    var1.set("初始化！")
    window.update()
    global thread
    thread = threading.Thread(target=downloader.implicit_download,args=(download_path,url,pdf_name, window, var1, int(scale.get())))
    thread.setDaemon(True)
    thread.start()


if __name__=="__main__":
    window = tk.Tk()
    window.geometry("650x391")
    window.title("教参平台下载工具")
    window.maxsize(width=650,height=391)
    window.minsize(width=650,height=391)    
    image = Image.open("bk.png")
    photo = ImageTk.PhotoImage(image)

    background = tk.Label(
        window,
        image=photo,
        compound = tk.CENTER,
    )
    
    background.pack()
    
    var1 = tk.StringVar()
    var1.set("本软件仅用于编程使用\n发售盗版内容者承担一切法律责任！")

    label1 = tk.Label(
        window,
        text="网址",
        background="#F7F7F7",
        font=tkFont.Font(family='ComicSansMS', size=20, weight=tkFont.BOLD)
    )

    label1.place(
        anchor="n",
        x=150,
        y=20
    )
    entry1 = tk.Entry(
        window,
        font=tkFont.Font(family='ComicSansMS', size=20, weight=tkFont.BOLD)
    )
    entry1.place(
        anchor="n",
        x=325,
        y=20
    )
    label2 = tk.Label(
        window,
        text="书名",
        background="#F7F7F7",
        font=tkFont.Font(family='ComicSansMS', size=20, weight=tkFont.BOLD)
    )
    label2.place(
        anchor="n",
        x=150,
        y=80
    )
    entry2 = tk.Entry(
        window,
        font=tkFont.Font(family='ComicSansMS', size=20, weight=tkFont.BOLD)
    )

    entry2.place(
        anchor="n",
        x=325,
        y=80
    )

    label4 = tk.Label(
        window,
        text="线程数",
        background="#F7F7F7",
        font=tkFont.Font(family='ComicSansMS', size=20, weight=tkFont.BOLD)
    )

    label4.place(
        anchor="n",
        x=130,
        y=150
    )

    scale = tk.Scale(
        window,from_=1,
        to=32,
        tickinterval=4,
        orient=tk.HORIZONTAL,
        length=280)
    
    scale.place(
        anchor="n",
        x = 325,
        y = 140
    )
    button = tk.Button(
        window,
        text='下载',
        command=begin,
        width=5,
        font=tkFont.Font(family='ComicSansMS', size=30, weight=tkFont.BOLD)
    )
    button.place(
        anchor="n",
        x=325,
        y=210
    )
    label3 = tk.Label(
        window,
        textvariable=var1,
        background="#F7F7F7",
        font=tkFont.Font(family='ComicSansMS', size=20, weight=tkFont.BOLD)
    )
    label3.place(
        anchor="n",
        x=325,
        y=260
    )
    window.mainloop()

