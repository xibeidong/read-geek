# -*- coding: utf-8 -*-

from pywinauto.application import Application

app = Application(backend="uia").connect(
    handle=0x000A0056)

dlg = app["Form1"]

# dlg.print_control_identifiers()

list1 = dlg.child_window(auto_id="listView1", control_type="List")
print(dir(list1.wrapper_object()))

list1.print_control_identifiers()

item = list1.get_item(0)
print(dir(item))
print("====================")

c_count = list1.column_count()

cur_c = 1
for item in list1.items():
    cur_c += 1
    print(item.texts(), end=" ")
    if cur_c > c_count:
        print()
        cur_c = 1
