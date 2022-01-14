import os
import shutil


try:
    import img2pdf

except:
    import os
    os.system('sudo pip3 install img2pdf')
    import img2pdf



def get_url_nums(driver,):
    url_num = 0
    while True:
        url_num+=1
        try:
            element = driver.find_element_by_xpath(f"/html/body/pre/a[{url_num+1}]")
        except:
            url_num-=1
            break
    return url_num


# reference : https://blog.csdn.net/zhuoqingjoking97298/article/details/110222668


def gen_pdf(pdf_name , pdf_path, page_list = []):
    imgs = []
    if len(pdf_name)==0:
        pdf_name = "untitled"
        remove(pdf_path+os.path.sep+pdf_name+".pdf")
    with open(pdf_path+os.path.sep+pdf_name+".pdf","wb") as f:
        f.write(img2pdf.convert(page_list))

def mkdir(dir_name):
    try:
        os.mkdir(dir_name)
    except:
        shutil.rmtree(dir_name)
        os.mkdir(dir_name)

def remove(file_name):
    try:
        os.remove(file_name)
    except:
        return 