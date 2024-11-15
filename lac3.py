import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# إعداد نافذة GUI
root = tk.Tk()
root.title("Image Processing GUI")
root.geometry("1000x600")
root.configure(bg="white")

# إعداد الإطارات
frame_buttons = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
frame_buttons.pack(side="left", fill="y")

frame_buttonss = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
frame_buttonss.pack(side="left", fill="y", padx=10)

frame_display = tk.Frame(root, bg="white", width=800, height=600)
frame_display.pack(side="right", expand=True, fill="both")
frame_display.pack_propagate(False)  # تثبيت حجم إطار العرض

def display_image(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image_rgb)
    image_pil = image_pil.resize((600, 400), Image.Resampling.LANCZOS)  # تغيير حجم الصورة لتناسب الإطار
    image_tk = ImageTk.PhotoImage(image_pil)
    panel.config(image=image_tk)
    panel.image = image_tk

# تحميل صورة جديدة
def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        global img
        img = cv2.imread(file_path)
        if img is None:
            messagebox.showerror("Error", "Failed to load image. Please select a valid image file.")
        else:
            display_image(img)

# تطبيق العمليات
def edge_detection():
    edges = cv2.Canny(img, 100, 200)
    display_image(edges)

def filtering():
    filtered = cv2.GaussianBlur(img, (5, 5), 0)
    display_image(filtered)

def thinning():
    thin = cv2.ximgproc.thinning(img)
    display_image(thin)

def pruning():
    kernel = np.ones((5, 5), np.uint8)
    pruned = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    display_image(pruned)

def noise_removal():
    denoised = cv2.fastNlMeansDenoising(img, None, 30, 7, 21)
    display_image(denoised)

def image_enhancement():
    enhanced = cv2.equalizeHist(img)
    display_image(enhanced)

def image_segmentation():
    ret, segmented = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    display_image(segmented)

def structuring_element():
    kernel = np.ones((5, 5), np.uint8)
    display_image(kernel * 255)

def erosion():
    kernel = np.ones((5, 5), np.uint8)
    eroded = cv2.erode(img, kernel, iterations=1)
    display_image(eroded)

def dilation():
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(img, kernel, iterations=1)
    display_image(dilated)

def opening():
    kernel = np.ones((5, 5), np.uint8)
    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    display_image(opened)

def closing():
    kernel = np.ones((5, 5), np.uint8)
    closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    display_image(closed)

def hit_and_miss():
    kernel = np.ones((5, 5), np.uint8)
    hitmiss = cv2.morphologyEx(img, cv2.MORPH_HITMISS, kernel)
    display_image(hitmiss)

def thickening():
    thick = cv2.dilate(img, np.ones((3, 3), np.uint8), iterations=1)
    display_image(thick)

# إضافة الأزرار للإطار الجانبي الأول
buttons = [
    ("Load Image", load_image),
    ("Edge Detection", edge_detection),
    ("Filtering", filtering),
    ("Thinning", thinning),
    ("Pruning", pruning),
    ("Noise Removal", noise_removal),
    ("Image Enhancement", image_enhancement),
    ("Image Segmentation", image_segmentation),
    ("Structuring Element", structuring_element),
    ("Erosion", erosion),
    ("Dilation", dilation)
]

# إضافة الأزرار للإطار الجانبي الثاني
buttonss = [
 
    ("Opening", opening),
    ("Closing", closing),
    ("Hit-and-Miss Operation", hit_and_miss),
    ("Thickening", thickening),
]

# إضافة الأزرار للإطار الأول
for (text, command) in buttons:
    button = tk.Button(frame_buttons, text=text, command=command, bg="black", fg="white", font=("Arial", 10, "bold"), padx=5, pady=5)
    button.pack(fill="x", pady=5)

# إضافة الأزرار للإطار الثاني
for (text, command) in buttonss:
    button = tk.Button(frame_buttonss, text=text, command=command, bg="black", fg="white", font=("Arial", 10, "bold"), padx=5, pady=5)
    button.pack(fill="x", pady=5)

# لوحة لعرض الصورة في الإطار الرئيسي
panel = tk.Label(frame_display, bg="white")
panel.pack(fill="both", expand=True)

root.mainloop()