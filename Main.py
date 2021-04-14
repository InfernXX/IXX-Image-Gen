from LargeImgGen import getlargeImg as glI
from SmallImgGen import getsmallImage as gsI
import Selector as Sc
from New_Algorithm import Overarching_Generate as OG
from Image_Integrity_Checker import Size_Check as S_I_C #Size Integrity Check
import time, os, webbrowser
from pathlib import Path
def Seeded_Gen():
    try:
        Temp_Time_Var = time.strftime(" %X on %d,%m,%Y",time.localtime()).replace(":", ";")
        Image_Name = "L.A;; "+Temp_Time_Var+" Image.png"
        glI(os.path.join(os.path.join(os.getcwd(),"Generated Images"),Image_Name))
        Integrity_Sorter(os.path.join(os.path.join(os.getcwd(),"Generated Images"),Image_Name))
        ICon = open("Integrity Config.IXXC", "r").read()
        if ICon == "N":
            pass
        elif ICon == "DiN":
            os.remove(os.path.join(os.path.join(os.getcwd(),"Generated Images"),Image_Name))
            pass
        elif ICon == "DiR":
            os.remove(os.path.join(os.path.join(os.getcwd(),"Generated Images"),Image_Name))
            Seeded_Gen()
        elif ICon == "KiR":
            Seeded_Gen()
        else:
            print("Saved as:",os.path.join(os.path.join(os.getcwd(),"Generated Images"),Image_Name))
    except Exception as The_Problem:
        File = open("Error Log.IXXLF", "a")
        Write_Var = "\n"+time.strftime(" @ %X on %d/%m/%Y; an Exception was caught: ",time.localtime())+str(The_Problem)
        File.write(Write_Var)
def UnSeeded_Gen():
    try:
        Temp_Time_Var = time.strftime(" %X on %d,%m,%Y",time.localtime()).replace(":", ";")
        Image_Name = "S.A;; "+Temp_Time_Var+" Image.png"
        gsI(os.path.join(os.path.join(os.getcwd(),"Generated Images"),Image_Name))
        Integrity_Sorter(os.path.join(os.path.join(os.getcwd(),"Generated Images"),Image_Name))
        ICon = open("Integrity Config.IXXC", "r").read()
        if ICon == "N":
            pass
        elif ICon == "DiN":
            os.remove(os.path.join(os.path.join(os.getcwd(),"Generated Images"),Image_Name))
            pass
        elif ICon == "DiR":
            os.remove(os.path.join(os.path.join(os.getcwd(),"Generated Images"),Image_Name))
            UnSeeded_Gen()
        elif ICon == "KiR":
            UnSeeded_Gen()
        else:
            print("Saved as:",os.path.join(os.path.join(os.getcwd(),"Generated Images"),Image_Name))
    except Exception as The_Problem:
        File = open("Error Log.IXXLF", "a")
        Write_Var = "\n"+time.strftime(" @ %X on %d/%m/%Y; an Exception was caught: ",time.localtime())+str(The_Problem)
        File.write(Write_Var)
def Integrity_Sorter(ImageName):
    File_True, Given_Size = S_I_C(ImageName)
    if File_True:
        pass
    else:
        print("Warning: File Size incorrect.")
        if Given_Size == "1x1":
            print("There will be no image, just a blank 1x1 image.")
        else:
            print("The image size is as followed:",Given_Size)
        print("You may choose what to do:")
        Sc.Quad_SelectSC("Do Nothing", "Delete Image and Nothing", "Delete Image and Generate a New Image", "Keep Image and Generate a New Image","N", "DiN", "DiR", "KiR", False, "450x125", True, "Integrity Config", "Integrity Config", ".IXXC", True, True, "IXX Image Gen Icon.ico")
def Main():
    #Mast_Con = open("Img_Config.IXXC", "r").read().split("\n")
    Check = Path(os.path.join(os.getcwd(),"Generated Images")).is_dir()
    if Check:
        pass
    else:
        os.mkdir(os.path.join(os.getcwd(),"Generated Images"))
    while True:
        ICon = open("Integrity Config.IXXC", "w")
        ICon.write(".")
        ICon.close()
        Sc.Hex_SelectSC("UnSeeded", "Seeded", "Organic-Like/Looking", "Open Config", "Open Selected Image Folder", "Quit Program", "uS", "S", "Ol", "OC", "OD", "E", False, "300x100", True, "Image Generator", "Config", ".IXXC", True, True, "IXX Image Gen Icon.ico")
        Con = open("Config.IXXC", "r").read()
        if Con == "uS":
            UnSeeded_Gen()
        elif Con == "S":
            Seeded_Gen()
        elif Con == "Ol":
            OG("Img_Config.IXXC")
        elif Con == "OC":
            os.startfile("Img_Config.IXXC")
        elif Con == "OD":
            open(os.path.join(os.getcwd(),"Generated Images"))
        elif Con == "E":
            break
        else:
            pass
Main()