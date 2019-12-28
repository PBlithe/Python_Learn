import os


class FileBackup(object):
    '''文本文件备份'''

    def __init__(self,src,dist):
        '''
        构造方法
        :param src: 目录 需要备份的文件目录
        :param dist: 目录 备份后的目录
        '''
        self.src = src
        self.dist = dist

    def read_files(self):
        '''读取src目录夏的所有文件'''
        ls = os.listdir(self.src) #获取当前目录下所有文件和目录
        for i in ls:
            self.backup_file(i)

    def backup_file(self,file_name):
        '''
        处理备份
        :param file_name: 文件/文件夹的名称
        :return:
        '''
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print('指定目录不存在，创建完成')
        full_src_path = os.path.join(self.src,file_name)
        full_dist_path = os.path.join(self.dist,file_name)
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[1].lower() == '.txt':
            with open(full_dist_path,'w',encoding='utf-8') as f_dist:
                print('>>开始备份[{}]'.format(file_name))
                with open(full_src_path,'r',encoding='utf-8') as f_src:
                    while True:
                        rest = f_src.read(100)
                        if not rest:
                            break
                        f_dist.write(rest)
                print('>>>[{}]备份完成'.format(file_name))
        else:
            print('{}不符合备份要求，跳过>>'.format(file_name))

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.abspath(__file__)) #获取当前文件的上级目录
    src_path = os.path.join(base_path,'src') #源文件目录
    dist_path = os.path.join(base_path,'dist') #目标文件目录

    fileBackup = FileBackup(src_path,dist_path)
    fileBackup.read_files()