import cv2 as cv
import mss
import mss.tools
from mss import mss as ms
from PIL import Image
coords = [(888,515), (1656,947)]
with ms() as sct:
    monitor = {'top': coords[0][1], 'left' : coords[0][0], 'width': int(coords[1][0] - coords[0][0]), 'height': int(coords[1][1] - coords[0][1])}
    f = sct.grab(monitor)
    png = mss.tools.to_png(f.rgb, f.size)
         
    img = Image.frombytes("RGB", f.size, f.bgra, "raw", "BGRX")
    img.save('h.png')
#img = cv.imread(png)
