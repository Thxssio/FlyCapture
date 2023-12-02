from pyflycap2.interface import GUI

gui = GUI()
ret = gui.show_selection()
guid = ret[1][0]  
print(guid)