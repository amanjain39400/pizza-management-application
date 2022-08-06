from PIL import Image, ImageTk
import tkinter as tk

#------------------------------------------------------------------------------
# Code to simulate background process periodically updating the image file.
# Note: 
#   It's important that this code *not* interact directly with tkinter 
#   stuff in the main process since it doesn't support multi-threading.
import itertools
import os
import shutil
import threading
import time

def update_image_file(dst):
    """ Overwrite (or create) destination file by copying successive image 
        files to the destination path. Runs indefinitely. 
    """
    TEST_IMAGES = 'p1.png', 'p2.png', 'p4.png'

    for src in itertools.cycle(TEST_IMAGES):
        shutil.copy(src, dst)
        time.sleep(1)  # pause between updates
#------------------------------------------------------------------------------

def refresh_image(canvas, img, image_path, image_id):
    try:
        pil_img = Image.open(image_path).resize((400,400), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(pil_img)
        canvas.itemconfigure(image_id, image=img)
    except IOError:  # missing or corrupt image file
        img = None
    # repeat every half sec
    canvas.after(500, refresh_image, canvas, img, image_path, image_id)  

root = tk.Tk()
image_path = 'p5.png'

#------------------------------------------------------------------------------
# More code to simulate background process periodically updating the image file.
th = threading.Thread(target=update_image_file, args=(image_path,))
th.daemon = True  # terminates whenever main thread does
th.start()
while not os.path.exists(image_path):  # let it run until image file exists
    time.sleep(.1)
#------------------------------------------------------------------------------

canvas = tk.Canvas(root, height=400, width=400)
img = None  # initially only need a canvas image place-holder
image_id = canvas.create_image(200, 200, image=img)
canvas.pack()

refresh_image(canvas, img, image_path, image_id)
root.mainloop()
