import tkinter as tk
from tkinter import filedialog

'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()

Folderpath = filedialog.askdirectory() #获得选择好的文件夹
Filepath = filedialog.askopenfilename() #获得选择好的文件

print('Folderpath:',Folderpath)
print('Filepath:',Filepath)

