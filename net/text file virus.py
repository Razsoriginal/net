import time
import os
import random 

def error(): 
    with open("error.txt") as f:
        f.write("This is an error message.\n")

    while True:
        error()
        time.sleep(0.5)

def openf():
    for i in range(10): 
        filename = "error_{}.txt".format(i)
        with open(filename, )