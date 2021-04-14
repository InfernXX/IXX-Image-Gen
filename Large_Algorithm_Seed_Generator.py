import time
import random as R
def Seed_Grabber(Mode):
    if Mode == "Time" or Mode == "time":
        return int(1000*time.time())
    elif Mode == "Random" or Mode == "random":
        Non_Deci_Len = R.randint(4, 13)
        for i in range(2):
            if i == 0:
                for I in range(Non_Deci_Len):
                    if I == 0:
                        R1 = "1" #R1 = Random Minimum
                    else:
                        R1 = str(R1)+"0"
            else:
                for i in range(Non_Deci_Len):
                    if i == 0:
                        R2 = "9" #R2 = Random Maximum
                    else:
                        R2 = str(R2)+"9"
        FR1 = R.randint(int(R1), int(R2)) #FR1 = Final Random Number(int)
        FR2 = R.uniform(0.0000, 0.9999) #FR2 = Final Random Number(Float)
        return int(float(FR1)+FR2)