import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Filter App")
        self.root.geometry("600x600")
        
        self.image_cv = None

        self.canvas = tk.Canvas(root, width=500, height=500, bg="lightgray")
        self.canvas.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        # Buttons
        btn_load = tk.Button(self.button_frame, text="Load Image", command=self.load_image)
        btn_load.grid(row=0, column=0, padx=5)

        btn_gray = tk.Button(self.button_frame, text="Grayscale", command=lambda: self.apply_filter("gray"))
        btn_gray.grid(row=0, column=1, padx=5)

        btn_blur = tk.Button(self.button_frame, text="Blur", command=lambda: self.apply_filter("blur"))
        btn_blur.grid(row=0, column=2, padx=5)

        btn_edges = tk.Button(self.button_frame, text="Edge Detection", command=lambda: self.apply_filter("edges"))
        btn_edges.grid(row=0, column=3, padx=5)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_cv = cv2.imread(file_path)
            self.display_image(self.image_cv)

    def apply_filter(self, filter_type):
        if self.image_cv is None:
            return

        if filter_type == "gray":
            processed = cv2.cvtColor(self.image_cv, cv2.COLOR_BGR2GRAY)
        elif filter_type == "blur":
            processed = cv2.GaussianBlur(self.image_cv, (5, 5), 0)
        elif filter_type == "edges":
            processed = cv2.Canny(self.image_cv, 100, 200)

        self.display_image(processed, is_gray=(filter_type == "gray" or filter_type == "edges"))

    def display_image(self, img, is_gray=False):
        if not is_gray:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img)
        img_pil = img_pil.resize((500, 500))
        img_tk = ImageTk.PhotoImage(img_pil)
        self.canvas.create_image(0, 0, anchor="nw", image=img_tk)
        self.canvas.image = img_tk

root = tk.Tk()
app = ImageFilterApp(root)
root.mainloop()
