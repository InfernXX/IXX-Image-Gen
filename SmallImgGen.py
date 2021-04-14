import numpy as np, random
from PIL import Image
import random as R
File = open("Img_Config.IXXC", "r").read().split("\n")
Sizes = [File[0].split(":"), File[1].split(":")]
Default_File_Ext = File[7].split(":")[1]

dX, dY = int(Sizes[0][1]), int(Sizes[1][1])
xArray = np.linspace(0.0, 1.0, dX).reshape((1, dX, 1))
yArray = np.linspace(0.0, 1.0, dY).reshape((dY, 1, 1))

def randColor():
    return np.array([random.random(), random.random(), random.random()]).reshape((1, 1, 3))
def getX(): return xArray
def getY(): return yArray
def safeDivide(a, b):
    return np.divide(a, np.maximum(b, 0.001))

functions = [(0, randColor),
             (0, getX),
             (0, getY),
             (1, np.sin),
             (1, np.cos),
             (2, np.add),
             (2, np.subtract),
             (2, np.multiply),
             (2, safeDivide)]
depthMin = 2
depthMax = 10

def buildSImg(depth = 0):
    funcs = [f for f in functions if
                (f[0] > 0 and depth < depthMax) or
                (f[0] == 0 and depth >= depthMin)]
    nArgs, func = random.choice(funcs)
    args = [buildSImg(depth + 1) for n in range(nArgs)]
    return func(*args)

def getsmallImage(Name, imgM=buildSImg):
    img = imgM

    # Ensure it has the right dimensions, dX by dY by 3
    try:
        img = np.tile(img, (dX / img.shape[0], dY / img.shape[1], 3 / img.shape[2]))
    except:
        pass

    # Convert to 8-bit, send to PIL and save
    img8Bit = np.uint8(np.rint(img(R.uniform(0.0, 1.0)) * 255.0))
    if ".png" in Name or ".jpg" in Name or ".jpeg" in Name or ".bmp" in Name or ".gif" in Name:
        Image.fromarray(img8Bit).save(Name)
    else:
        Image.fromarray(img8Bit).save(Name+Default_File_Ext)