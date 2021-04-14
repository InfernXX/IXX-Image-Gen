from PIL import Image
import math, random, time, sys, os
def Overarching_Generate(Config_File="Config.IXXC", CutomDir="Generated Images"):
    Con = open(Config_File, "r").read().split("\n")
    Res = [Con[0].split(":"), Con[1].split(":")]
    ResX = int(Res[0][1])
    ResY = int(Res[1][1])
    Pixel_Cycle = int(Con[2].split(":")[1])
    RGB_Bal_Temp_Var = [Con[3].split(":"), Con[4].split(":"), Con[5].split(":")]
    RBal = int(RGB_Bal_Temp_Var[0][1])
    GBal = int(RGB_Bal_Temp_Var[1][1])
    BBal = int(RGB_Bal_Temp_Var[2][1])
    First_Cycle_Balence = bool(Con[6].split(":")[1])
    t = time.time()
    print(time.strftime("Starting time: %X on %d,%m,%Y",time.localtime()))

    def clamp(n, smallest, largest): 
        return round(max(smallest, min(n, largest)))

    resolution = (ResX, ResY)

    img = Image.new(mode="RGB",size=(resolution[0],resolution[1]))

    ppx = resolution[0]//2
    ppy = resolution[1]//2

    if First_Cycle_Balence:
        r = random.randint(0, RBal)
        b = random.randint(0, GBal)
        g = random.randint(0, BBal)
    elif First_Cycle_Balence is not True:
        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)
    else:
        print("Exception Raised: No Valid Config Bool Var Inputted.")
        print("Reverting to 'False' status...")
        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)
    for i in range(Pixel_Cycle):
        img.putpixel((ppx,ppy),(r,g,b))

        dirx = random.choice([0,-1,1])
        diry = random.choice([0,-1,1])

        ppx = clamp(ppx + dirx,0,resolution[0]-1)
        ppy = clamp(ppy + diry,0,resolution[1]-1)

        r = clamp(r + random.choice([0,-1,1]),0,RBal)
        g = clamp(g + random.choice([0,-1,1]),0,GBal)
        b = clamp(b + random.choice([0,-1,1]),0,BBal)

    Temp_Time_Var = time.strftime(" %X on %d,%m,%Y",time.localtime()).replace(":", ";")
    Image_Name = os.path.join(os.path.join(os.getcwd(), CutomDir), "Image"+Temp_Time_Var+".png")
    img.save(Image_Name)

    print(f"Done! Took {time.time() - t} seconds and is saved under the file name: {Image_Name}.")
    print(time.strftime("Finishing time: %X on %d,%m,%Y",time.localtime()))
    return Image_Name
