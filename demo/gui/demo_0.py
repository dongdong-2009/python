from tkinter import *
import hashlib

def gui_start():
    init_window = Tk()        #实例化出一个父窗口
    init_window.title("物联网云平台:Akon")
    init_window.geometry('1000x500+20+300')  # 290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
    init_window["bg"] = "lightblue"  # 窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
    init_window.attributes("-alpha", 2)  # 虚化 值越小虚化程度越高
    init_window.mainloop()    #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()