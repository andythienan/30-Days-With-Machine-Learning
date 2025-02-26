import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, Scale, Button, Label, Frame
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
def bai1():
    print("Bài 1: Đọc, hiển thị và lưu ảnh")
    
    # Đọc ảnh từ máy tính
    img = cv2.imread('image.jpg')
    
    if img is None:
        print("Không thể đọc ảnh. Vui lòng kiểm tra đường dẫn.")
        return
    
    # Hiển thị ảnh
    cv2.imshow('Ảnh gốc', img)
    
    # Lưu ảnh với định dạng khác
    cv2.imwrite('image_converted.png', img)
    print("Đã lưu ảnh với định dạng mới: image_converted.png")
    
    # Đợi cho đến khi người dùng nhấn phím bất kỳ
    cv2.waitKey(0)
    cv2.destroyAllWindows()