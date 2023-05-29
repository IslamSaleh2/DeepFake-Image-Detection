from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox


def load_clicked():
    filename = filedialog.askopenfilename(title ='load image')
    entry0.delete(0, END)
    entry0.insert(0, filename)
    file=open("file.txt","w")
    file.write(filename)
    file.close()
    
def GAN_clicked():
   import Real_Fake.py

def CopyandMove_clicked():
   import Testing_copyandmove_Model.py

def Morphing_clicked():
   import Morphing.py
    
def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("688x498")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 498,
    width = 688,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    343.5, 48.5,
    text = "DeepFake Detection",
    fill = "#000000",
    font = ("Roboto-Medium", int(18.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 260, y = 437,
    width = 172,
    height = 50)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = GAN_clicked,
    relief = "flat")

b1.place(
    x = 105, y = 239,
    width = 168,
    height = 48)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = Morphing_clicked,
    relief = "flat")

b2.place(
    x = 105, y = 342,
    width = 168,
    height = 48)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = CopyandMove_clicked,
    relief = "flat")

b3.place(
    x = 378, y = 239,
    width = 168,
    height = 48)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 380, y = 342,
    width = 168,
    height = 48)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = load_clicked,
    relief = "flat")

b5.place(
    x = 43, y = 105,
    width = 590,
    height = 85)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    299.5, 161.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 53, y = 146,
    width = 493,
    height = 28)

window.resizable(False, False)
window.mainloop()
