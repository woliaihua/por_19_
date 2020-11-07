
import chardet
def get_temp_dict():
    """
    获取需要 填写的文本信息
    :return: 字典
    """
    def get_file_code(filename):
        f3 = open(filename, 'rb')
        data = f3.read()
        encode = chardet.detect(data).get('encoding')
        f3.close()
        return encode

    dict1 = {}
    with open('template.txt','r',encoding=get_file_code('template.txt')) as f:
        for line in f.readlines():
            if line:
                try:
                    l =line.split('：')
                    dict1[l[0].strip()] = l[1].strip('\n')
                except:
                    pass
    return dict1
if __name__ == '__main__':
    get_temp_dict()