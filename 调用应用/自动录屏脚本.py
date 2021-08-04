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

from datetime import datetime
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler

#EV课程录制，每天晚上8点开启到凌晨两点自动关闭
#系统时间
# #记得走的时候关闭音乐声音，会影响课程录制

#
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
#开zoom，进入会议
def zoom():
    app=get_pid("Zoom.exe")
    print (app)
    # app = Application().connect(process=get_pid("pythonw.exe"))
    #开启程序
    if app==2:
        app_dir = r'D:\anzhuang\pymol\PyMOLWin.exe'
        open_app(app_dir)
        time.sleep(1)
    app = get_pid("Zoom.exe")
    # 打开ZOOM
    # 获取窗口
    handle = win32gui.FindWindow(None, "Zoom Cloud Meetings")
    # 查找窗口句柄的方法， win32gui.FindWindow.——win32gui.Findwindow(param1,param2)：param1需要传入窗口的类名，param2需要传入窗口的标题
    # 显示窗口
    win32gui.ShowWindow(handle, 4)
    # 显示窗口 win32gui.ShowWindow
    # #获取窗口大小
    list = win32gui.GetWindowRect(handle)
    # 返回窗口位置：left,top,right,botton
    # 移动鼠标
    pyautogui.moveTo(list[0] + 250, list[1] + 200, duration=0.5)
    # 鼠标点击
    pyautogui.click()
    pyautogui.moveTo(list[0] + 250, list[1] + 150, duration=0.5)
    pyautogui.click()
    # 输入会议号
    k = PyKeyboard()
    k.type_string('Z54adf4L')
    k.tap_key(k.enter_key)
#开录屏
def Recording_screen():
    pyautogui.moveTo(50 , 50, duration=0.5)
    pyautogui.moveTo(70, 30, duration=0.5)
    pyautogui.click()
def Turn_off_recording_screen():
    pyautogui.moveTo(50 , 50, duration=0.5)
    pyautogui.moveTo(90, 30, duration=0.5)
    pyautogui.click()
#
def timedTask():
    '''
    第一个参数: 延迟多长时间执行任务(单位: 秒)86400一天
    第二个参数: 要执行的任务, 即函数
    第三个参数: 调用函数的参数(tuple)
    '''
    Timer(86400 , task, ()).start()

# 定时任务：录屏 晚八点
def task1():
    # #开会议
    zoom()
    # #开启录屏
    Recording_screen()
    # time.sleep(10)
#定时任务： 关录屏 凌晨两点
def task2():
    #关录屏
    Turn_off_recording_screen()
def task3():
    print("ceshi")
if __name__ == "__main__":
    scheduler = BackgroundScheduler()


    # 5月18
    scheduler.add_job(task1, 'date', run_date=datetime(2021, 5, 18, 20, 5, 0))
    scheduler.add_job(task2, 'date', run_date=datetime(2021, 5, 19, 2, 30, 0))
    #5月19
    scheduler.add_job(task1, 'date', run_date=datetime(2021, 5, 19, 20, 5, 0))
    scheduler.add_job(task2, 'date', run_date=datetime(2021, 5, 20, 2, 30, 0))
    # 5月20
    scheduler.add_job(task1, 'date', run_date=datetime(2021, 5, 20, 20, 5, 0))
    scheduler.add_job(task2, 'date', run_date=datetime(2021, 5, 21, 2, 30, 0))
    #5月21
    scheduler.add_job(task1, 'date', run_date=datetime(2021, 5, 21, 20, 5, 0))
    scheduler.add_job(task2, 'date', run_date=datetime(2021, 5, 22, 2, 30, 0))

    scheduler.start()
    print("Waiting to exit")
    while True:
        time.sleep(1)


