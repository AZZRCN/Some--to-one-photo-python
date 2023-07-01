#from io import BytesIO
import tkinter as tk
from tkinter import Button, Entry
from tkinter import filedialog
import os
from typing import List
from PIL import Image
from tkinter.messagebox import askyesnocancel
from 最小公倍数 import lcm
root = tk.Tk()
imagelist:list[str] = []
successlater=["jpeg","png","jpg","ico","bmp","tiff"]
label = tk.Label(root)
label.grid(column=1, row=1, columnspan=3)


def update():
    temp = ""
    for i in imagelist:
        temp += (str(i)+"\n")
    if (temp == ""):
        temp = "这里还没有东西哦"
    else:
        temp = temp[:-1]
    label.configure(text=temp)
    del temp
    if (len(imagelist) == 0):
        test3["state"] = "disabled"
    else:
        test3["state"] = "normal"


def instr():
    global test, test2, test3
    test["state"] = "disabled"
    test2["state"] = "disabled"
    test3["state"] = "disabled"
    enter = Entry(root)
    enter.grid(column=1, row=3, columnspan=3)
    def incomplate():
        nonlocal acceptButton, helpfindButton, enter
        global test, test2, test3
        t = enter.get()
        if (os.access(t, os.F_OK) and t.split(".")[-1] in successlater):
            test["state"] = "normal"
            test2["state"] = "normal"
            test3["state"] = "normal"
            acceptButton.destroy()
            del acceptButton
            helpfindButton.destroy()
            del helpfindButton
            enter.destroy()
            del enter
            imagelist.append(t)
            update()
        else:
            enter.delete('0', 'end')
            enter.insert("0", "错误的路径")
    acceptButton = Button(root, text="提交", command=incomplate)
    acceptButton.grid(column=1, row=4)
    def helpfind():
        t = filedialog.askopenfilenames()  # str
        if (not all(t)):
            return
        if(type(t) == str):
            enter.delete('0', 'end')
            enter.insert('0', t[2:-3])
        else:
            for i in t:
                imagelist.append(i)
            update()
    helpfindButton = Button(root, text="帮助寻找", command=helpfind)
    helpfindButton.grid(column=2, row=4)


def delobj():
    del imagelist[len(imagelist)-1]
    update()
def makeobj():
    #ansimage = Image.new('RGB',(20,20))
    idea = askyesnocancel("设置模式","是->宽\n否->高")
    if(idea == None):return
    elif(idea):#tempw,w,cnt,th,tl,t,tn
        tempw = []
        for i in imagelist:
            t = Image.open(i, "r").convert('RGB') # 读取并指定模式为RGB
            tempw.append(t.size[0])
        w = lcm(tempw)
        cnt = 0
        th = []
        tl = []
        for i in imagelist:
            t = Image.open(i, "r").convert('RGB') # 读取并指定模式为RGB
            tn = t.size
            tl.append(t.resize((w, round(w / tn[0] * tn[1])))) # 转换为整数，四舍五入
            th.append(round(w / tn[0] * tn[1]))
        ansimage = Image.new('RGB', (w, sum(th)))
        for i in tl:
            ansimage.paste(i, (0, sum(th[:cnt]))) # 粘贴位置更改为 (0, sum(th￼))
            cnt += 1
        ansimage.show()
            
        
    else:
        temph = []
        for i in imagelist:
            temph.append(Image.open(i).size[1])
        h = lcm(temph)
        for i in imagelist:
            t = Image.open(i,"r")
            tl = t.size
            t.resize((h,int(h/tl[1]*tl[0]))).show()

test = tk.Button(root, text="update", command=update)
test.grid(column=2, row=2)
test2 = tk.Button(root, text="write", command=instr)
test2.grid(column=1, row=2)
test3 = tk.Button(root, text="delete", command=delobj)
test3.grid(column=3, row=2)
update()
test4=tk.Button(root, text="make", command=makeobj)
test4.grid(column=4, row=2)
root.mainloop()

"""import numpy as np
from PIL import Image
from io import BytesIO
import requests
img1_url = 'https://nbjice.oss-cn-hangzhou.aliyuncs.com/10-sansheng/202001/9a594e5c-2dca-11ea-a72d-00163e09d976.jpg'
im2_url = 'https://nbjice.oss-cn-hangzhou.aliyuncs.com/10-sansheng/201912/e84203ee-255e-11ea-a72d-00163e09d976.png'

# 通过二进制流读取图片
img1=Image.open(BytesIO(requests.get(img1_url).content))
# 改变图像尺寸
img1 = img1.resize((640, 360))
img2=Image.open(BytesIO(requests.get(img2_url).content))
img2 = img2.resize((180, 180))
# 合并两个图像，img2 放到 img1上面 并指定坐标
img1.paste(img2, (430, 90))
# 展示图像
img1.show()"""
#aiter()
#anext()
#breakpoint()