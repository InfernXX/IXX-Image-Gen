from PIL import Image as I
Con = open("Img_Config.IXXC", "r").read().split("\n")
Sizes = [int(Con[0].split(":")[1]), int(Con[1].split(":")[1])]
def Size_Check(Image_Name):
    Img = I.open(Image_Name)
    W, H = Img.size
    if W == 1 and H == 1:
        return False, "1x1"
    elif W > Sizes[0] or H > Sizes[1] or W < Sizes[0] or H > Sizes[1]:
        return False, str(W)+"x"+str(H)
    else:
        return True, str(Sizes[0])+"x"+str(Sizes[1])