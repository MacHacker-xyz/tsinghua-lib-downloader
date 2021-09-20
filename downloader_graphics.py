import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import downloader
import threading
from PIL import Image,ImageTk

#"http://reserves.lib.tsinghua.edu.cn/book5//00001042/00001042000/mobile/index.html"
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
    thread = threading.Thread(target=downloader.implicit_download,args=(download_path,url,pdf_name, window, var1))
    thread.start()


if __name__=="__main__":
    window = tk.Tk()
    window.geometry("650x391")
    window.title("教参平台爬虫")
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
    label1 = tk.Label(
        window,
        text="网址",
        background="#F7F7F7",
        font=tkFont.Font(family='ComicSansMS', size=20, weight=tkFont.BOLD)
    )
    label1.place(
        anchor="n",
        x=325,
        y=0
    )
    entry1 = tk.Entry(
        window,
        font=tkFont.Font(family='ComicSansMS', size=20, weight=tkFont.BOLD)
    )
    entry1.place(
        anchor="n",
        x=325,
        y=40
    )
    label2 = tk.Label(
        window,
        text="书名",
        background="#F7F7F7",
        font=tkFont.Font(family='ComicSansMS', size=20, weight=tkFont.BOLD)
    )
    label2.place(
        anchor="n",
        x=325,
        y=80
    )
    entry2 = tk.Entry(
        window,
        font=tkFont.Font(family='ComicSansMS', size=20, weight=tkFont.BOLD)
    )

    entry2.place(
        anchor="n",
        x=325,
        y=120
    )
    label_warning = tk.Label(
        window,
        text="本软件仅供学习编程知识\n发售盗版内容者承担一切法律责任",
        fg="Red",
        background="#F7F7F7",
        font=tkFont.Font(family='ComicSansMS', size=20, weight=tkFont.BOLD)
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
        width=5,
        font=tkFont.Font(family='ComicSansMS', size=30, weight=tkFont.BOLD)
    )
    button.place(
        anchor="n",
        x=325,
        y=240
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
        y=290
    )
    window.mainloop()