#coding=utf-8
#!/usr/bin/python
import os
import win32gui
# -*- coding: UTF8 -*-
from pywinauto import Application
import psutil
import pyautogui
import time
from pykeyboard import *
#寻找进程
def get_pid(name):

    #  作用：根据进程名判断是否存在进程pid
    #  返回：2不存在，1存在
    # '''
    sig=2
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        process_name = p.name()
        if process_name==name:
            sig=1
            break
    return sig

#输入命令
def winfun(hwnd, lparam):
    s = win32gui.GetWindowText(hwnd)
    if len(s) > 3:
        print("winfun, child_hwnd: %d   txt: %s" % (hwnd, s))
        if s=="QWidgetClassWindow":
            list =win32gui.GetWindowRect(hwnd)
            print(list)
            #输入命令
            pyautogui.moveTo(list[0] + 10, list[1] + 100, duration=0.5)
            pyautogui.click()
            k = PyKeyboard()
            k.type_string('abcdefg')
            k.tap_key(k.enter_key)
    return 1
#打开程序
def open_app(app_dir):
    os.startfile(app_dir)
if __name__ == "__main__":
    app=get_pid("pythonw.exe")
    print (app)
    # app = Application().connect(process=get_pid("pythonw.exe"))
    #开启程序
    if app==2:
        app_dir = r'D:\anzhuang\pymol\PyMOLWin.exe'
        open_app(app_dir)
        time.sleep(1)
    #关闭弹窗
    # handleAct = win32gui.FindWindow(None, "Activation")
    # time.sleep(1)
    # win32gui.CloseWindow(handleAct)
    #获取窗口
    handle = win32gui.FindWindow(None,"PyMOL")
    win32gui.ShowWindow(handle,4)
    #输入命令
    list = win32gui.GetWindowRect(handle)
    print(list)
    pyautogui.moveTo(list[0] + 20, list[1] + 100, duration=0.5)
    pyautogui.click()
    k = PyKeyboard()
    k.type_string('abcdefg')
    k.tap_key(k.enter_key)

    # subHandle = win32gui.FindWindowEx(handle, 0, None, '')
    # print(subHandle)

    #
    # menuHandle = win32gui.GetMenu(subHandle)
    # print(subHandle)
    # print(menuHandle)


