import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
from keras.models import load_model

model = load_model('traffic_classifier.h5')

# dictionary to label all traffic signs class.
classes = {1: 'Speed limit (20km/h)',
           2: 'Speed limit (30km/h)',
           3: 'Speed limit (50km/h)',
           4: 'Speed limit (60km/h)',
           5: 'Speed limit (70km/h)',
           6: 'Speed limit (80km/h)',
           7: 'End of speed limit (80km/h)',
           8: 'Speed limit (100km/h)',
           9: 'Speed limit (120km/h)',
           10: 'No passing',
           11: 'No passing veh over 3.5 tons',
           12: 'Right-of-way at intersection',
           13: 'Priority road',
           14: 'Yield',
           15: 'Stop',
           16: 'No vehicles',
           17: 'Veh > 3.5 tons prohibited',
           18: 'No entry',
           19: 'General caution',
           20: 'Dangerous curve left',
           21: 'Dangerous curve right',
           22: 'Double curve',
           23: 'Bumpy road',
           24: 'Slippery road',
           25: 'Road narrows on the right',
           26: 'Road work',
           27: 'Traffic signals',
           28: 'Pedestrians',
           29: 'Children crossing',
           30: 'Bicycles crossing',
           31: 'Beware of ice/snow',
           32: 'Wild animals crossing',
           33: 'End speed + passing limits',
           34: 'Turn right ahead',
           35: 'Turn left ahead',
           36: 'Ahead only',
           37: 'Go straight or right',
           38: 'Go straight or left',
           39: 'Keep right',
           40: 'Keep left',
           41: 'Roundabout mandatory',
           42: 'End of no passing',
           43: 'End no passing veh > 3.5 tons'}

# GUI initialization
top = tk.Tk()
top.geometry('850x650')
top.title('Traffic Sign Recognition')
top.configure(background='#2F4F4F')
label = Label(top, background='#2F4F4F', font=('arial', 15, 'bold'))
sign = Label(top)


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = Image.resize(30, 30)
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model.predict_classes([image])[0]
    sign = classes[pred + 1]
    print(sign)
    label.configure(foreground='$011638', text='Sign')


# show classify button
def class_button(file_path):
    classify_button = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=6)
    classify_button.configure(background='#DCDCDC', foreground='black', font=('arial', 10, 'bold'))
    classify_button.place(relx=0.79, rely=0.39)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign.configure(image=im)
        sign.image = im
        label.configure(text='')
        class_button(file_path)
    except:
        pass


upload = Button(top, text="Upload Image", command=upload_image, padx=10, pady=5)
upload.configure(background='#DCDCDC', foreground='black', font=('arial', 10, 'bold'))
upload.pack(side=BOTTOM, pady=50)
sign.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Traffic Sign Recognition", pady=20, font=('arial', 38, 'bold'))
heading.configure(background='#2F4F4F', foreground='#DCDCDC')
heading.pack()
top.mainloop()