import os
from tkinter import *
from tkinter import filedialog
import hashlib
from RSA import rsa
from Components import Components
from RSA import rsa
root = Tk()
root.title("Chu ki dien tu RSA")
root.geometry("1500x700")
root.configure(bg="#fff")
root.resizable(False, False)


lb1 = Label(root, text="PHÁT SINH CHỮ KÝ", bg='white', font=('Calibri', 20, 'bold'))
lb1_1 = Label(root, text="KIỂM TRA CHỮ KÝ", bg='white', font=('Calibri', 20, 'bold'))
lb2 = Label(root, text="Văn bản ký", bg='white', font=('Calibri', 10))
lb3 = Label(root, text="Chữ ký", bg='white', font=('Calibri', 10))
van_ban_ki = Text(root, width=30, height=6, bd=2)
chu_ky = Text(root, width=30, height=6, bd=2)

label2 = Label(root, text="Văn bản kí", bg='white', font=('Calibri', 10))
label3 = Label(root, text="Chữ kí", bg='white', font=('Calibri', 10))
label4 = Label(root, text="Thông báo", bg='white', font=('Calibri', 10))
ky_van_ban_screen = Text(root, width=30, height=6, bd=2)
chu_ky_screen = Text(root, width=30, height=6, bd=2)
thong_bao_screen = Text(root, width=30, height=6, bd=2)

canvas = Canvas(root,width=2,height=700,bg="black")
canvas.create_line(650,100,650,700)
def file_explorer():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("Text file", "*.txt"),("Word file","*.docs")))
    os.startfile(filename)

def ky():
    text_sign = van_ban_ki.get("1.0","end-1c")
    text_ki = chu_ky.get("1.0","end-1c")
    if len(text_ki) != 0:
        chu_ky.delete('1.0', END)
    if len(text_sign) > 0:
        text = rsa.RSA_sign(text_sign)
    else:
        text = "Don't have text!!!!"
    chu_ky.insert(END, text)


def luu_file_ky():
    text = chu_ky.get("1.0","end-1c")
    file = open("file/file_ky.txt", "w")
    file.write(text)
    file.close()
def move():
    chu_ky_screen.insert(END,chu_ky.get("1.0", "end-1c"))

def check():
    text1 = ky_van_ban_screen.get("1.0","end-1c")
    text2 = chu_ky_screen.get("1.0", "end-1c")
    result = rsa.ss(text1, text2)
    thong_bao_screen.insert(END, result)


btn1 = Button(root, text="File", background="blue", font=('Calibri', 8), width=10, padx=10, pady=10,fg='#ffffff', command=file_explorer)
btn2 = Button(root, text="Ký", background="blue", font=('Calibri', 8), width=10, padx=10, pady=10, fg='#ffffff', command=ky)
btn3 = Button(root, text="Chuyển", background="blue", font=('Calibri', 8), width=10, padx=10, pady=10, fg='#ffffff',command=move)
btn4 = Button(root, text="Lưu", background="blue", font=('Calibri', 8), width=10, padx=10, pady=10,fg='#ffffff', command=luu_file_ky)

bt1 = Button(root, text="File văn bản", background="blue", font=('Calibri', 8), width=10, padx=10, pady=10,fg='#ffffff', command=file_explorer)
bt2 = Button(root, text="File chữ ký", background="blue", font=('Calibri', 8), width=10, padx=10, pady=10,fg='#ffffff', command=file_explorer)
bt3 = Button(root, text="Kiểm tra chữ ký", background="blue", font=('Calibri', 8), width=10, padx=10, pady=10,fg='#ffffff', command=check)


lb1.place(x=300, y=0)
lb1_1.place(x=1000, y=0)
lb2.place(x=40, y=80)
lb3.place(x=40, y=280)
van_ban_ki.place(x=150, y=80)
chu_ky.place(x=150, y=280)

label2.place(x=800,y=80)
label3.place(x=800,y=280)
label4.place(x=800,y=480)
ky_van_ban_screen.place(x=900, y=80)
chu_ky_screen.place(x=900, y=280)
thong_bao_screen.place(x=900, y=480)

btn4.place(x=500, y=360)
btn1.place(x=500, y=100)
btn3.place(x=500, y=300)
btn2.place(x=220, y=210)

bt1.place(x=1200, y=100)
bt2.place(x=1200, y=300)
bt3.place(x=1000, y=400)

canvas.pack()
root.mainloop()

