import os
import utils
import shutil
import multi_thread
import imghdr

def implicit_download(dir_path, url,pdf_name, window, var, scale):
    try:
        download(dir_path, url,pdf_name, window, var, scale)
    except:
        var.set("下载失败!")
        window.update()

def download(dir_path, url, pdf_name, window, var, scale):
    chapter_num = 0
    page_number = []
    utils.mkdir("tmp")
    page_list = []
    stop_flag = False
    for i in range(1000):
        if stop_flag:
            os.removedirs("tmp"+os.path.sep+str(i-1))
            break
        chapter_url = url[:-21]+"{:0>3d}".format(i)+"/files/mobile/"
        os.mkdir("tmp"+os.path.sep+str(i))
        chapter_num+=1
        page_number.append(0)
    
        for j in range(1,1000):
            page_url = chapter_url+str(j)+".jpg"
            page_number[chapter_num-1]+=1
            var.set(f"正在下载第{chapter_num}章第{page_number[chapter_num-1]}页")
            window.update()
            data_folder = "tmp"+os.path.sep+str(i)
            thread_num = scale
            downloader = multi_thread.DownloadFile(page_url, data_folder, thread_num)
            downloader.main()
            while(True):
                if os.path.exists("tmp"+os.path.sep+str(i)+os.path.sep+str(j)+".jpg"):
                    break
            size = os.path.getsize("tmp"+os.path.sep+str(i)+os.path.sep+str(j)+".jpg")
            if imghdr.what("tmp"+os.path.sep+str(i)+os.path.sep+str(j)+".jpg")==None:
                os.remove("tmp"+os.path.sep+str(i)+os.path.sep+str(j)+".jpg")
                if j == 1:
                    stop_flag = True
                    break
                else:
                    break
            page_list.append("tmp"+os.path.sep+str(i)+os.path.sep+str(j)+".jpg")
            
    utils.gen_pdf(page_list = page_list,pdf_name = pdf_name,pdf_path=dir_path)
    shutil.rmtree("tmp")
    var.set(f"下载完成！\n共下载{chapter_num}章{sum(page_number)}页\n保存到{dir_path+os.path.sep+pdf_name+'.pdf'}")
    window.update()