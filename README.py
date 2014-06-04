import Tkinter
import tkMessageBox

f = open('README.txt')
s = f.read()
f.close()

tkMessageBox.showinfo("AnniversaryReminder: README" , s)
