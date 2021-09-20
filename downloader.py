import requests
import os
import wget
import utils
import shutil
def implicit_download(dir_path, url,pdf_name, window, var):
    try:
        download(dir_path, url,pdf_name, window, var)
    except:
        var.set("下载失败!")
        window.update()

def download(dir_path, url, pdf_name, window, var):
    chapter_num = 0
    page_number = []
    utils.mkdir("tmp")
    page_list = []
    for i in range(1000):
        chapter_url = url[:-21]+"{:0>3d}".format(i)+"/files/mobile/"
        r=requests.get(chapter_url+"1.jpg",timeout=5)
        code = r.status_code
        if code == 200:
            print ('OK 网站访问正常')
            os.mkdir("tmp"+os.path.sep+str(i))
            chapter_num+=1
            page_number.append(0)
        else:
            break
    
        for j in range(1,1000):
            page_url = chapter_url+str(j)+".jpg"
            try:
                page_number[chapter_num-1]+=1
                var.set(f"正在下载第{chapter_num}章第{page_number[chapter_num-1]}页")
                window.update()
                wget.download(page_url,"tmp"+os.path.sep+str(i))
                page_list.append("tmp"+os.path.sep+str(i)+os.path.sep+str(j)+".jpg")
                print("tmp"+os.path.sep+str(i)+os.path.sep+str(j)+".jpg")
            except:
                break
    utils.gen_pdf(page_list = page_list,pdf_name = pdf_name,pdf_path=dir_path)
    shutil.rmtree("tmp")
    var.set(f"下载完成！\n共下载{chapter_num}章{sum(page_number)}页\n保存到{dir_path+os.path.sep+pdf_name+'.pdf'}")
    window.update()