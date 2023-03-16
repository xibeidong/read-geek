# -*- coding: utf-8 -*-

from pywinauto.application import Application

#
file = open("./111.CSV", "w", encoding='utf-8')
# 使用spy++工具获取到句柄
# 句柄连接应用，也可以用pid，或者直接用脚本打开应用
app = Application(backend="uia").connect(
    handle=0x001107DE)

# 不用这种方式，因为geek这类软件打开的时候会开启两个进程，一个32位，一个64位，会绑定错
# app = Application(backend="uia").start(
#     "D:\Program Custom\geek.exe", timeout=5)

# 获取窗体
dlg = app["Geek Uninstaller 1.5.1.163"]

# 查看dlg的全部控件，如果控件太多，打印会覆盖
# dlg.print_control_identifiers()

# 获取child_window
list1 = dlg.child_window(class_name="SysListView32")

# 打印list1的方法属性
# print(dir(list1.wrapper_object()))

# list1.print_control_identifiers()

# item = list1.get_item(0)
# print(dir(item))
# print("====================")

c_count = list1.column_count()

cur_c = 1
for item in list1.items():
    cur_c += 1
    print(item.texts(), end=" ")
    str = ','.join(item.texts())
    print(str)
    file.writelines(str+'\n')
    if cur_c > c_count:
        print()
        cur_c = 1

file.close()
