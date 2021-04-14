import tkinter as T
from tkinter import Text,filedialog
#InfernXX(Dyllan Morgan)'s Tkinter Configuation Selector. Use for easy selection of Specific options for your Programs.
#The 'SC' at the end of various Selectors means 'Self Closing'. The File Selection Class is Self Closing by default with no way to change it at present.

#Self Closing Button Selectors
class Duel_SelectSC:
    def __init__(self, ButName1, ButName2, Param1, Param2, Append=False, Geo="100x100", 
    HaveCustomTitle=False, CustomTitle="Duel Selector(Auto Close)", CustomConfig="Config.txt", CustomConfigFilePrefix=".txt", HaveCustomConfigFilePreifx=False):
        self.Param1 = Param1
        self.Param2 = Param2
        self.Append = Append
        self.ConfigFile = CustomConfig
        if ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx is not True:
            self.ConfigFile += ".txt"
        elif ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx:
            try:
                F = open(self.ConfigFile, "r")
                F.close()
                pass
            except FileNotFoundError:
                self.ConfigFile += CustomConfigFilePrefix
        self.root = T.Tk()
        if HaveCustomTitle:
            self.root.title(str(CustomTitle))
        else:
            self.root.title("Duel Selector(Auto Close)")
        self.root.geometry(str(Geo))
        Button1 = T.Button(self.root, text=str(ButName1), command=self.Opt1)
        Button2 = T.Button(self.root, text=str(ButName2), command=self.Opt2)
        Button1.pack()
        Button2.pack()
        self.root.mainloop()
    def Opt1(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param1)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param1)
            F.close()
        self.root.destroy()
    def Opt2(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param2)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param2)
            F.close()
        self.root.destroy()

class Tri_SelectSC:
    def  __init__(self, ButName1, ButName2, ButName3, Param1, Param2, Param3, Append=False, Geo="100x100", 
    HaveCustomTitle=False, CustomTitle="Triple Selector(Auto Close)", CustomConfig="Config.txt", CustomConfigFilePrefix=".txt", HaveCustomConfigFilePreifx=False):
        self.Param1 = Param1
        self.Param2 = Param2
        self.Param3 = Param3
        self.Append = Append
        self.ConfigFile = CustomConfig
        if ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx is not True:
            self.ConfigFile += ".txt"
        elif ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx:
            try:
                F = open(self.ConfigFile, "r")
                F.close()
                pass
            except FileNotFoundError:
                self.ConfigFile += CustomConfigFilePrefix
        self.root = T.Tk()
        if HaveCustomTitle:
            self.root.title(str(CustomTitle))
        else:
            self.root.title("Triple Selector(Auto Close)")
        self.root.geometry(str(Geo))
        Button1 = T.Button(self.root, text=str(ButName1), command=self.Opt1)
        Button2 = T.Button(self.root, text=str(ButName2), command=self.Opt2)
        Button3 = T.Button(self.root, text=str(ButName3), command=self.Opt3)
        Button1.pack()
        Button2.pack()
        Button3.pack()
        self.root.mainloop()
    def Opt1(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param1)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param1)
            F.close()
        self.root.destroy()
    def Opt2(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param2)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param2)
            F.close()
        self.root.destroy()
    def Opt3(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param3)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param3)
            F.close()
        self.root.destroy()

class Quad_SelectSC:
    def  __init__(self, ButName1, ButName2, ButName3, ButName4, Param1, Param2, Param3, Param4, Append=False, Geo="100x100", 
    HaveCustomTitle=False, CustomTitle="Quadruple Selector(Auto Close)", CustomConfig="Config.txt", CustomConfigFilePrefix=".txt", HaveCustomConfigFilePreifx=False, HaveCustomIcon=False, CustomIconPath=""):
        self.Param1 = Param1
        self.Param2 = Param2
        self.Param3 = Param3
        self.Param4 = Param4
        self.Append = Append
        self.ConfigFile = CustomConfig
        if ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx is not True:
            self.ConfigFile += ".txt"
        elif ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx:
            try:
                F = open(self.ConfigFile, "r")
                F.close()
                pass
            except FileNotFoundError:
                self.ConfigFile += CustomConfigFilePrefix
        self.root = T.Tk()
        if HaveCustomTitle:
            self.root.title(str(CustomTitle))
        else:
            self.root.title("Quadruple Selector(Auto Close)")
        self.root.geometry(str(Geo))
        Button1 = T.Button(self.root, text=str(ButName1), command=self.Opt1)
        Button2 = T.Button(self.root, text=str(ButName2), command=self.Opt2)
        Button3 = T.Button(self.root, text=str(ButName3), command=self.Opt3)
        Button4 = T.Button(self.root, text=str(ButName4), command=self.Opt4)
        Button1.pack()
        Button2.pack()
        Button3.pack()
        Button4.pack()
        if HaveCustomIcon:
            import os
            self.root.iconbitmap(os.path.join(os.path.join(os.getcwd(), "Assets"), CustomIconPath))
        self.root.mainloop()
    def Opt1(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param1)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param1)
            F.close()
        self.root.destroy()
    def Opt2(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param2)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param2)
            F.close()
        self.root.destroy()
    def Opt3(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param3)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param3)
            F.close()
        self.root.destroy()
    def Opt4(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param4)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param4)
            F.close()
        self.root.destroy()

class Hex_SelectSC():
    def __init__(self, ButName1, ButName2, ButName3, ButName4, ButName5, ButName6, Param1, Param2, Param3, Param4, Param5, Param6, Append=False, Geo="250x125", 
    HaveCustomTitle=False, CustomTitle="Hextuple Selector(Auto Close)", CustomConfig="Config.txt", CustomConfigFilePrefix=".txt", HaveCustomConfigFilePreifx=False, HaveCustomIcon=False, CustomIconPath=""):
        self.Param1 = Param1
        self.Param2 = Param2
        self.Param3 = Param3
        self.Param4 = Param4
        self.Param5 = Param5
        self.Param6 = Param6
        self.Append = Append
        self.ConfigFile = CustomConfig
        if ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx is not True:
            self.ConfigFile += ".txt"
        elif ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx:
            try:
                F = open(self.ConfigFile, "r")
                F.close()
                pass
            except FileNotFoundError:
                self.ConfigFile += CustomConfigFilePrefix
        self.root = T.Tk()
        if HaveCustomTitle:
            self.root.title(str(CustomTitle))
        else:
            self.root.title("Hextuple Selector(Auto Close)")
        self.root.geometry(str(Geo))
        Button1 = T.Button(self.root, text=str(ButName1), command=self.Opt1)
        Button2 = T.Button(self.root, text=str(ButName2), command=self.Opt2)
        Button3 = T.Button(self.root, text=str(ButName3), command=self.Opt3)
        Button4 = T.Button(self.root, text=str(ButName4), command=self.Opt4)
        Button5 = T.Button(self.root, text=str(ButName5), command=self.Opt5)
        Button6 = T.Button(self.root, text=str(ButName6), command=self.Opt6)
        Button1.grid(row=1, column=0)
        Button2.grid(row=2, column=0)
        Button3.grid(row=3, column=0)
        Button4.grid(row=1, column=1)
        Button5.grid(row=2, column=1)
        Button6.grid(row=3, column=1)
        if HaveCustomIcon:
            import os
            self.root.iconbitmap(os.path.join(os.path.join(os.getcwd(), "Assets"), CustomIconPath))
        self.root.mainloop()
    def Opt1(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param1)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param1)
            F.close()
        self.root.destroy()
    def Opt2(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param2)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param2)
            F.close()
        self.root.destroy()
    def Opt3(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param3)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param3)
            F.close()
        self.root.destroy()
    def Opt4(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param4)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param4)
            F.close()
        self.root.destroy()
    def Opt5(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param5)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param5)
            F.close()
        self.root.destroy()
    def Opt6(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param6)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param6)
            F.close()
        self.root.destroy()

#Non-Self Closing Button Selectors
class Duel_Select:
    def __init__(self, ButName1, ButName2, Param1, Param2, Append=False, Geo="100x100", 
    HaveCustomTitle=False, CustomTitle="Duel Selector", CustomConfig="Config.txt", CustomConfigFilePrefix=".txt", HaveCustomConfigFilePreifx=False):
        self.Param1 = Param1
        self.Param2 = Param2
        self.Append = Append
        self.ConfigFile = CustomConfig
        if ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx is not True:
            self.ConfigFile += ".txt"
        elif ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx:
            try:
                F = open(self.ConfigFile, "r")
                F.close()
                pass
            except FileNotFoundError:
                self.ConfigFile += CustomConfigFilePrefix
        self.root = T.Tk()
        if HaveCustomTitle:
            self.root.title(str(CustomTitle))
        else:
            self.root.title("Duel Selector")
        self.root.geometry(str(Geo))
        Button1 = T.Button(self.root, text=str(ButName1), command=self.Opt1)
        Button2 = T.Button(self.root, text=str(ButName2), command=self.Opt2)
        Button1.pack()
        Button2.pack()
        self.root.mainloop()
    def Opt1(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param1)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param1)
            F.close()
    def Opt2(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param2)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param2)
            F.close()

class Tri_Select:
    def  __init__(self, ButName1, ButName2, ButName3, Param1, Param2, Param3, Append=False, Geo="100x100", 
    HaveCustomTitle=False, CustomTitle="Triple Selector", CustomConfig="Config.txt", CustomConfigFilePrefix=".txt", HaveCustomConfigFilePreifx=False):
        self.Param1 = Param1
        self.Param2 = Param2
        self.Param3 = Param3
        self.Append = Append
        self.ConfigFile = CustomConfig
        if ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx is not True:
            self.ConfigFile += ".txt"
        elif ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx:
            try:
                F = open(self.ConfigFile, "r")
                F.close()
                pass
            except FileNotFoundError:
                self.ConfigFile += CustomConfigFilePrefix
        self.root = T.Tk()
        if HaveCustomTitle:
            self.root.title(str(CustomTitle))
        else:
            self.root.title("Triple Selector")
        self.root.geometry(str(Geo))
        Button1 = T.Button(self.root, text=str(ButName1), command=self.Opt1)
        Button2 = T.Button(self.root, text=str(ButName2), command=self.Opt2)
        Button3 = T.Button(self.root, text=str(ButName3), command=self.Opt3)
        Button1.pack()
        Button2.pack()
        Button3.pack()
        self.root.mainloop()
    def Opt1(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param1)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param1)
            F.close()
    def Opt2(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param2)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param2)
            F.close()
    def Opt3(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param3)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param3)
            F.close()

class Quad_Select:
    def  __init__(self, ButName1, ButName2, ButName3, ButName4, Param1, Param2, Param3, Param4, Append=False, Geo="100x100", 
    HaveCustomTitle=False, CustomTitle="Quadruple Selector", CustomConfig="Config.txt", CustomConfigFilePrefix=".txt", HaveCustomConfigFilePreifx=False):
        self.Param1 = Param1
        self.Param2 = Param2
        self.Param3 = Param3
        self.Param4 = Param4
        self.Append = Append
        self.ConfigFile = CustomConfig
        if ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx is not True:
            self.ConfigFile += ".txt"
        elif ".txt" not in self.ConfigFile and HaveCustomConfigFilePreifx:
            try:
                F = open(self.ConfigFile, "r")
                F.close()
                pass
            except FileNotFoundError:
                self.ConfigFile += CustomConfigFilePrefix
        self.root = T.Tk()
        if HaveCustomTitle:
            self.root.title(str(CustomTitle))
        else:
            self.root.title("Quadruple Selector")
        self.root.geometry(str(Geo))
        Button1 = T.Button(self.root, text=str(ButName1), command=self.Opt1)
        Button2 = T.Button(self.root, text=str(ButName2), command=self.Opt2)
        Button3 = T.Button(self.root, text=str(ButName3), command=self.Opt3)
        Button4 = T.Button(self.root, text=str(ButName4), command=self.Opt4)
        Button1.pack()
        Button2.pack()
        Button3.pack()
        Button4.pack()
        self.root.mainloop()
    def Opt1(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param1)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param1)
            F.close()
    def Opt2(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param2)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param2)
            F.close()
    def Opt3(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param3)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param3)
            F.close()
    def Opt4(self):
        if self.Append:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+self.Param4)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(self.Param4)
            F.close()

#File Selectors
class File_Select:
    def __init__(self, FTypeA='', FTypeB='', FTypeC='', FTypeD='', FTypeE='', WindowTitle="Please Select a File.", HaveCustomDir=False, CustomDir="Desktop", CustomConfig="Config.txt", CustomConfigFilePrefix=".txt"):
        self.FTyA = str(FTypeA)
        self.FTyB = str(FTypeB)
        self.FTyC = str(FTypeC)
        self.FTyD = str(FTypeD)
        self.FTyE = str(FTypeE)
        self.ConfigFile = CustomConfig
        if ".txt" not in self.ConfigFile and CustomConfigFilePrefix == ".txt":
            self.ConfigFile += ".txt"
        elif ".txt" not in self.ConfigFile and CustomConfigFilePrefix != ".txt":
            self.ConfigFile += str(CustomConfigFilePrefix)
        if HaveCustomDir:
            self.Dir = str(CustomDir)
        else:
            self.Dir = "Desktop"
        if str(self.FTyA) != '' and str(self.FTyB) != '' and str(self.FTyC) != '' and str(self.FTyD) != '' and str(self.FTyE) != '':
            fileName = filedialog.askopenfilename(initialdir=self.Dir, title=str(WindowTitle), 
            filetypes=((self.FTyA.capitalize()+" Files","."+self.FTyA), (self.FTyB.capitalize()+" Files","."+self.FTyB), (self.FTyC.capitalize()+" Files","."+self.FTyC), (self.FTyD.capitalize()+" Files","."+self.FTyD), (self.FTyE.capitalize()+" Files","."+self.FTyE), ("All Files","*,*")))
            ReadTextName = fileName
        elif self.FTyA != '' and self.FTyB != '' and self.FTyC != '' and self.FTyD != '':
            fileName = filedialog.askopenfilename(initialdir=self.Dir, title=str(WindowTitle), 
            filetypes=((self.FTyA.capitalize()+" Files","."+self.FTyA), (self.FTyB.capitalize()+" Files","."+self.FTyB), (self.FTyC.capitalize()+" Files","."+self.FTyC), (self.FTyD.capitalize()+" Files","."+self.FTyD), ("All Files","*,*")))
            ReadTextName = fileName
        elif self.FTyA != '' and self.FTyB != '' and self.FTyC != '':
            fileName = filedialog.askopenfilename(initialdir=self.Dir, title=str(WindowTitle), 
            filetypes=((self.FTyA.capitalize()+" Files","."+self.FTyA), (self.FTyB.capitalize()+" Files","."+self.FTyB), (self.FTyC.capitalize()+" Files","."+self.FTyC), ("All Files","*,*")))
            ReadTextName = fileName
        elif self.FTyA != '' and self.FTyB != '':
            fileName = filedialog.askopenfilename(initialdir=self.Dir, title=str(WindowTitle), 
            filetypes=((self.FTyA.capitalize()+" Files","."+self.FTyA), (self.FTyB.capitalize()+" Files","."+self.FTyB), ("All Files","*,*")))
            ReadTextName = fileName
        else:
            fileName = filedialog.askopenfilename(initialdir=self.Dir, title=str(WindowTitle), 
            filetypes=((self.FTyA.capitalize()+" Files","."+self.FTyA), ("All Files","*,*")))
            ReadTextName = fileName
        try:
            File = open(str(self.ConfigFile), "r")
            F = File.readlines()
            if F[0] != '':
                SkipLine = True
            else:
                SkipLine = False
        except:
            F = open(str(self.ConfigFile), "w")
            F.close()
            SkipLine = False
        if SkipLine:
            F = open(str(self.ConfigFile), "a")
            F.write("\n"+ReadTextName)
            F.close()
        else:
            F = open(str(self.ConfigFile), "w")
            F.write(ReadTextName)
            F.close()