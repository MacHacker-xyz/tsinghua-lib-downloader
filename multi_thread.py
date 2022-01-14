import os
import time
from threading import Thread
 
#自动下载缺失的库
try:
    import httpx
except:
    import os
    os.system('sudo pip3 install httpx')
    import httpx

class DownloadFile(object):
    def __init__(self, download_url, data_folder, thread_num):
        """
        :param download_url: 文件下载连接
        :param data_folder: 文件存储目录
        :param thread_num: 开辟线程数量
        """
        self.download_url = download_url
        self.data_folder = data_folder
        self.thread_num = thread_num
        self.file_size = None
        self.cut_size = None
        self.thread_list = []
        self.file_path = os.path.join(self.data_folder, download_url.split('/')[-1])
 
    def downloader(self, etag, thread_index, start_index, stop_index, retry=False):
        sub_path_file = "{}_{}".format(self.file_path, thread_index)
        if os.path.exists(sub_path_file):
            temp_size = os.path.getsize(sub_path_file)  # 本地已经下载的文件大小
        else:
            temp_size = 0
        if stop_index == '-': stop_index = ""
        headers = {'Range': 'bytes={}-{}'.format(start_index + temp_size, stop_index),
                   'ETag': etag, 'if-Range': etag,
                   }
        down_file = open(sub_path_file, 'ab')
        try:
            with httpx.stream("GET", self.download_url, headers=headers) as response:
                num_bytes_downloaded = response.num_bytes_downloaded
                for chunk in response.iter_bytes():
                    if chunk:
                        down_file.write(chunk)
                        num_bytes_downloaded = response.num_bytes_downloaded
        except Exception as e:
            print("Thread-{}:请求超时,尝试重连\n报错信息:{}".format(thread_index, e))
            self.downloader(etag, thread_index, start_index, stop_index, retry=True)
        finally:
            down_file.close()
        return
 
    def get_file_size(self):
        """
        获取预下载文件大小和文件etag
        :return:
        """
        with httpx.stream("GET", self.download_url) as response2:
            etag = ''
            total_size = int(response2.headers["Content-Length"])
            for tltle in response2.headers.raw:
                if tltle[0].decode() == "ETag":
                    etag = tltle[1].decode()
                    break
        return total_size, etag
 
    def cutting(self):
        """
        切割成若干份
        :param file_size: 下载文件大小
        :param thread_num: 线程数量
        :return:
        """
        cut_info = {}
        cut_size = self.file_size // self.thread_num
        for num in range(1, self.thread_num + 1):
            if num != 1:
                cut_info[num] = [cut_size, cut_size * (num - 1) + 1, cut_size * num]
            else:
                cut_info[num] = [cut_size, cut_size * (num - 1), cut_size * num]
            if num == self.thread_num:
                cut_info[num][2] = '-'
        return cut_info, cut_size
 
    def write_file(self):
        """
        合并分段下载的文件
        :param file_path:
        :return:
        """
        if os.path.exists(self.file_path):
            if len(self.file_path) >= self.file_size:
                return
        with open(self.file_path, 'ab') as f_count:
            for thread_index in range(1, self.thread_num + 1):
                with open("{}_{}".format(self.file_path, thread_index), 'rb') as sub_write:
                    f_count.write(sub_write.read())
                # 合并完成删除子文件
                os.remove("{}_{}".format(self.file_path, thread_index))
        return
 
    def create_thread(self, etag, cut_info):
        """
        开辟多线程下载
        :param file_path: 文件存储路径
        :param etag: headers校验
        :param cut_info:
        :return:
        """
 
        for thread_index in range(1, self.thread_num + 1):
            thread = Thread(target=self.downloader,
                            args=(etag, thread_index, cut_info[thread_index][1], cut_info[thread_index][2]))
 
            thread.setName('Thread-{}'.format(thread_index))
            thread.setDaemon(True)
            thread.start()
            self.thread_list.append(thread)
        for thread in self.thread_list:
            thread.join()
        return
 
    def check_thread_status(self):
        """
        查询线程状态。
        :return:
        """
        while True:
            for thread in self.thread_list:
                thread_name = thread.getName()
                if not thread.isAlive():
                    print("{}:已停止".format(thread_name))
            time.sleep(1)
 
    def create_data(self):
        if not os.path.exists(self.data_folder):
            os.mkdir(self.data_folder)
        return
 
    def main(self):
        # 平分几份
        self.create_data()
        self.file_size, etag = self.get_file_size()
        # 按线程数量均匀切割下载文件
        cut_info, self.cut_size = self.cutting()
        # 下载文件名称
        # 创建下载进度条
        # 开始多线程下载
        self.create_thread(etag, cut_info)
        # 合并多线程下载文件
        self.write_file()
        return 
 
if __name__ == '__main__':
    download_url = "https://releases.ubuntu.com/20.04/ubuntu-20.04.3-desktop-amd64.iso"
    data_folder = "/Users/houzhaobang/Desktop"
    thread_num = 32
    downloader = DownloadFile(download_url, data_folder, thread_num)
    try:
        downloader.main()
    except:
        print("在这里")
        pass