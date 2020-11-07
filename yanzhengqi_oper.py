from win32gui  import *
import win32con
from mouseToClick import MouseToClick

import win32gui_struct
import win32api
import win32gui
import win32clipboard as w
from  time import sleep
 # 生成 buffer 对象
class GetWindowMsg():
    def __init__(self,clasename,window_name):
        self.window_name = window_name
        self.handle = FindWindow(clasename, window_name)#获取窗口句柄
        self.shezhi()
        # self.title = GetWindowText(self.handle)#获取窗口标题
        # print(self.title)

    def shezhi(self):
        """
        设置窗口前台
        :return:
        """
        # 发送还原最小化窗口的信息
        win32gui.SendMessage(self.handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
        SetForegroundWindow(self.handle)  # 设置窗口前台
        ShowWindow(self.handle, 1)  # 显示窗口


    def find_idxSubHandle(self,pHandle, winClass, index=0):
        """
        已知子窗口的窗体类名
        寻找第index号个同类型的兄弟窗口
        :param pHandle: 父级窗口，不一定是最顶层的
        :param winClass: 要查找的窗口类名
        :param index: 要查找的第几个窗口，比如有两个Button  即为 0，1
        :return:
        """
        assert type(index) == int and index >= 0
        handle = win32gui.FindWindowEx(pHandle, 0, winClass, None)
        while index > 0:
            handle = win32gui.FindWindowEx(pHandle, handle, winClass, None)
            index -= 1
        return handle


    def find_subHandle(self,pHandle, winClassList):
        """
        递归寻找子窗口的句柄
        pHandle是祖父窗口的句柄
        winClassList是各个子窗口的class列表，父辈的list - index小于子辈
        :param pHandle: 祖父窗口句柄，最外层句柄
        :param winClassList:  [ ( "ComboBoxEx32" , 1 ) , ( "ComboBox" , 0 ) , ( "Edit" , 0 ) ]#类名，index
        :return: 要查找的子窗体句柄
        """
        assert type(winClassList) == list
        if len(winClassList) == 1:
            return self.find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
        else:
            pHandle = self.find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
            return self.find_subHandle(pHandle, winClassList[1:])


    def get_edit_txt(self,hWnd):

        length = 10000
        buf = PyMakeBuffer(length)
        length2 = SendMessage(hWnd, win32con.WM_GETTEXT, length, buf)+1
        buf = PyMakeBuffer(length2)
        SendMessage(hWnd, win32con.WM_GETTEXT, length2, buf)
        #print('get: ', SendMessage(hWnd, win32con.WM_GETTEXT, length2, buf))

        address, length = PyGetBufferAddressAndLen(buf)
        text = PyGetString(address, length)

        print('获取到的编码: ', text)
        return text

def get_make_code(input_cod):
    #打开认证器
    G = GetWindowMsg('WTWindow', '日亚-谷歌认证器v1.0')
    clear_hd = G.find_subHandle(G.handle, [('Button', 0)])  # clear的句柄
    sleep(0.3)
    #点击清空
    PostMessage(clear_hd, win32con.BM_CLICK, 0, 0)  # 点击
    sleep(0.1)
    #输入编码
    edit_hd2 = G.find_subHandle(G.handle, [('Edit', 1)])  # 上面这个输入框的句柄
    win32gui.SendMessage(edit_hd2, win32con.WM_SETTEXT, None, input_cod)  # 输入内容
    sleep(0.1)
    #点击生成编码
    make_hd = G.find_subHandle(G.handle, [('Button', 1)])  # make的句柄
    PostMessage(make_hd, win32con.BM_CLICK, 0, 0)  # 点击
    sleep(0.1)
    edit_hd = G.find_subHandle(G.handle, [('Edit', 0)])  # 下面这个输入框的句柄
    #获取生成的code
    text = G.get_edit_txt(edit_hd)
    if text:
        return text.strip()
    else:
        sleep(0.5)
        text = G.get_edit_txt(edit_hd)
        return text.strip()
if __name__ == '__main__':
    print(get_make_code('5egdfgdgdfg123123fsdfsdfsdfsd fsdfsd fsdf sdf sdf d'))
    print(11111111111111)