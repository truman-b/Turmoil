#!/usr/bin/env python3

import os

def main():
    #open firefox 500 times this is just for a demonstration on why it is important to think before you execute. 
    for i in range(500):
        os.system("firefox &")
    #open up the terminal 500 times
    for i in range(500):
        os.system("gnome-terminal &")

if __name__ == "__main__":
    main()

