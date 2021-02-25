import math
import tkinter as tk
import numpy as np
from math import floor
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image
from numpy import asarray
from numpy import log2


def open_file():
    """Open an image to equalize"""
    filepath = askopenfilename(
        filetypes=[("Image", "*.png *.jpg"), ("PNG", "*.png"), ("JPEG", "*.jpg")]
    )
    if not filepath:
        return
    entry.delete("0", tk.END)
    entry.insert(tk.END, filepath)


def convert():
    """Convert using a simplified version of the Histogram Equalization"""
    filepath = entry.get()
    to_equalize = Image.open(filepath)
    to_equalize = to_equalize.convert('L')
    data = asarray(to_equalize)
    equalizedArray = np.empty_like(data)

    max_value = 0
    min_value = 0
    average = 0

    for i in range(int(data.size / data[0].size)):
        for j in range(data[0].size):
            if data[i][j] > max_value:
                max_value = data[i][j]
            if data[i][j] < min_value:
                min_value = data[i][j]
            average = average + data[i][j]

    average = int(average / data.size)
    delta_value = max_value - min_value
    shift_level = 8 - floor(log2(delta_value + 1))

    for i in range(int(data.size / data[0].size)):
        row = np.empty_like(data[0])
        for j in range(data[0].size):
            if average < 123:
                temp_pixel = int((data[i][j] - min_value) * math.pow(2, shift_level))
            else:
                temp_pixel = int((data[i][j] + min_value) / math.pow(2, shift_level))
            new_pixel = max(0, min(255, temp_pixel))
            row[j] = new_pixel
        equalizedArray[i] = row

    equalized = Image.fromarray(equalizedArray)
    equalized.save("Equalized.png", "PNG")


"""GUI handling with Tkinter"""
window = tk.Tk()
window.geometry("400x400")
window.title("PyImageEqualizer 1.0")
entry = tk.Entry(fg="black", bg="white", width=50)
pathButton = tk.Button(
    text="Open File",
    width=7,
    height=2,
    bg="white",
    fg="black",
    command=open_file,
)
convertButton = tk.Button(
    text="Equalize",
    width=50,
    height=4,
    bg="white",
    fg="black",
    command=convert,
)

entry.place(x=20, y=20)
entry.insert(0, "Paste image path here...")
pathButton.place(x=325, y=10)
convertButton.place(x=20, y=60)
window.mainloop()
