import sys

# python tesseract
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# tkinter
try:
    # python 3.0 +
    from tkinter import (Tk, Label,
                         Scrollbar, RIGHT,
                         filedialog, VERTICAL,
                         Button, Y, messagebox, LEFT, BOTH, BOTTOM, X, NONE, END, TOP
                         )
    import tkinter as tk
except ImportError:
    # python 2.7 -
    from Tkinter import (Tk, Label,
                         Scrollbar, RIGHT,
                         filedialog, VERTICAL,
                         Button, Y, messagebox
                         )
    import Tkinter as tk

# Pillow and Python-CV imports
from PIL import ImageTk, Image
import cv2

# PyDF2 Package
import PyPDF2


class Window(tk.Frame):
    # customizing tkinter frames and key bindings
    def __init__(self, master):
        self.master = master
        self.master.bind("<F11>", self.do_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.master.geometry("400x500+0+0")

    def do_fullscreen(self, event=None):
        self.master.wm_state('zoomed')
        fullscreen = self.master.wm_state('zoomed')
        self.master.title('Optical Character Recognition' + str(fullscreen))

    def end_fullscreen(self, event=None):
        self.master.wm_state('normal')
        default_screen = self.master.wm_state('normal')
        self.master.title('OCR' + str(default_screen))


def upload_image():
    # Image Upload Module
    try:
        path = filedialog.askopenfilename()
        image = Image.open(path)
        image.thumbnail((720, 480))
        img = ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image = img
        show_extract_button(path)
    except AttributeError:
        error_msg("Error: Please provide an image")
    except Exception as e:
        sys.exit(str(e))


def upload_pdf():
    # Pdf Upload Module
    try:
        path = filedialog.askopenfilename()
        pdf_file_obj = open(path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

        text = ""
        for page in pdf_reader.pages:
            print(pdf_reader.pages)
            text += page.extract_text() + "\n"
            print(text)
        scroll_Bar(text)

    except AttributeError:
        error_msg("Error: Please provide an File")
    except Exception as e:
        sys.exit(str(e))


def error_msg(error):
    # Error Handling Module
    messagebox.showerror('Error', error)


def extract(path):
    # Text Extraction
    try:
        original_img = cv2.imread(path)
        sample_img = cv2.resize(original_img, (400, 400))
    except Exception as e:
        sys.exit(str(e))
    im = preprocess_finale(sample_img)
    texts = pytesseract.image_to_data(im)
    mytext = ""
    prevy = 0
    for cnt, text in enumerate(texts.splitlines()):
        if cnt == 0:
            continue
        text = text.split()
        if len(text) == 12:
            x, y, w, h = int(text[6]), int(text[7]), int(text[8]), int(text[9])
            if len(mytext) == 0:
                prey = y
            if prevy - y >= 10 or y - prevy >= 10:
                print(mytext)
                Label(root, text=mytext, font=('Times New Roman', 15, 'bold')).pack()
                mytext = ""
            mytext = mytext + text[11] + " "
            prevy = y
    Label(root, text=mytext, font=('Times New Roman', 15, 'bold')).pack()


def preprocess_finale(im):
    # Image Filtering and Threshold functionalities with CV2 & Pillow
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    im = cv2.bilateralFilter(im, 5, 55, 60)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    _, im = cv2.threshold(im, 240, 255, 1)
    return im


# Extract Button
def show_extract_button(path):
    extractBtn = Button(root, text="Extract text", command=lambda: extract(path), bg="#009AEE", fg="white", pady=15,
                        borderwidth=5,
                        padx=15, font=('Times New Roman bold', 15, 'bold'))
    extractBtn.pack()


def scroll_Bar(text):
    h = Scrollbar(root, orient='horizontal')
    h.pack(side=BOTTOM, fill=X)
    v = Scrollbar(root)
    v.pack(side=RIGHT, fill=Y)
    t = tk.Text(root, width=100, height=100, wrap=NONE,
                xscrollcommand=h.set,
                yscrollcommand=v.set)
    t.insert(END, f"{text}\n")
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)


# Python Main Module
if __name__ == "__main__":
    root = Tk()

    # application icon
    root.iconbitmap("favicon.ico")

    # application title, root & scroll bar setup
    root.title('OCR')

    newline = Label(root, font=('Times New Roman bold', 20))

    uploaded_img = Label(root)

    frame = Window(root)

    # Initial Upload Button
    Button(root, text="Upload an image", command=upload_image, bg="#000000", fg="white", height=2, width=15,
           borderwidth=5,
           font=('Times New Roman bold', 15, 'bold')).pack()
    newline.configure(text='\n')
    newline.pack()
    Button(root, text="Upload an pdf", command=upload_pdf, bg="#000000", fg="white", height=2, width=15, borderwidth=5,
           font=('Times New Roman bold', 15, 'bold')).pack()
    newline.configure(text='\n')
    newline.pack()
    uploaded_img.pack()
    root.mainloop()
