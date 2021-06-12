#Librerie necessarie
import os
import time
from random import random

#Delay(for jokes)
Secondi = (input("Type the delay of program excecution (for trolling)"))
parent_dir = (input("Type folder creation path"))
time.sleep(int(Secondi))


while True:
    #parent_dir = "C:/folderOverflow"
    foldername = str("folder") + str(random())
    directory = foldername
    path = os.path.join(parent_dir, str(directory))
    path = os.path.join(parent_dir, str(foldername))
    os.mkdir(path)

