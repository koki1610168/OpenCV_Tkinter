from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog
import cv2

def select_image():
    global pane1A, pane1B

    path = tkinter.filedialog.askopenfilename()

    if len(path) > 0:
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 100)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image = Image.fromarray(image)
        edged = Image.fromarray(edged)

        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)

        if pane1A is None or pane1B is None:
            pane1A = Label(image=image)
            pane1A.image = image
            pane1A.pack(side="left", padx=10, pady=10)

            pane1B = Label(image=edged)
            pane1B.image = edged
            pane1B.pack(side="right", padx=10, pady=10)

        else:
            pane1A.configure(image=image)
            pane1B.configure(image=image)
            pane1A.image = image
            pane1B.image = edged

root = Tk()
pane1A = None
pane1B = None

btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

root.mainloop()