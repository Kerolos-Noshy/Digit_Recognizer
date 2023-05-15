import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageOps
from tensorflow.keras import models, preprocessing
import numpy as np

# Load the trained model
model = models.load_model('image_classifier_new.h5')


def predict_image_label(image_path):
    img = preprocessing.image.load_img(image_path, color_mode='rgb', target_size=(28, 28))
    # detect the color of the first pixel
    pixel = img.getpixel((0, 0))
    is_white = True
    for value in pixel:
        if value < 160:
            is_white = False
            break
    img = img.convert('L')  # convert image to grayscale

    # if color of first pixel is white then convert image color
    if is_white:
        img = ImageOps.invert(img)  # if the background is not black

    img_numpy = np.asarray(img)
    img_numpy = img_numpy.reshape(1, 28, 28)
    img_numpy = img_numpy / 255
    return np.argmax(model.predict(img_numpy))


# Define the function to select an image file
def select_file():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img = img.resize((300, 300))
    img = ImageTk.PhotoImage(img)
    canvas.itemconfigure(image_id, image=img)
    canvas.image = img
    digit = predict_image_label(file_path)
    digit_label.configure(text="Predicted number is: " + str(digit), font=12)


root = tk.Tk()
root.title("Digit Recognition")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
image = Image.new("RGB", (300, 300), "white")
img = ImageTk.PhotoImage(image)
image_id = canvas.create_image(0, 0, anchor="nw", image=img)

button = tk.Button(root, text="Select an Image File", command=select_file)
button.pack()

digit_label = tk.Label(root, text="")
digit_label.pack()

root.mainloop()


