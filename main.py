from tkinter import *
import tkinter.font as tf
import random

gp = []


def get_random_group():
    global gp
    for i in range(len(gp)):
        gp[i] = Label(root, text='')
        gp[i].place(x=130, rely=0.2 + i / 10, relwidth=0.8, relheight=0.1)
    group_size = int(inp1.get())

    namelist = '刘一 陈二 张三 李四 王五 赵六 孙七 周八 吴九 郑十 亲银 文茹 四怡 盖彬 花琦 迪曜 春尔 飞萌 翠杭 兰姬 慧清 付梓 晨溪'
    namelist = namelist.split(' ')
    random.shuffle(namelist)

    group_number = len(namelist) // group_size

    group_list = [[] for i in range(group_number)]

    i = 0
    for name in namelist:
        group_list[i].append(name)
        i += 1
        if (i == group_number):
            i = 0

    gp = []
    for group_i in range(len(group_list)):
        s = "第%d组:\t" % (group_i + 1)
        for member in group_list[group_i]:
            s += member + '\t'
        gp.append(Label(root, text=s, font='微软雅黑 -30 bold'))
        gp[group_i].place(x=130, rely=0.15 + group_i / 15,
                          relwidth=0.8, relheight=0.1)

    inp1.delete(0, END)


root = Tk()
root.geometry('1800x1000')
root.title('随机分组器')

lb1 = Label(root, text='请输入每组人数')
lb1.place(relx=0.25, rely=0.06, width=240, height=30)
inp1 = Entry(root)
inp1.place(relx=0.45, rely=0.06, width=90, height=30)

btn1 = Button(root, text='生成随机分组', command=get_random_group)
btn1.place(relx=0.60, rely=0.06, width=90, height=30)

root.mainloop()
