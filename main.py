from time import sleep
import psutil
import tkinter as tk
from tkinter import messagebox # not imported when we import tk

def main():
    root = tk.Tk()
    root.withdraw()
    PROCNAME = "LeagueClient"
    while True:
        for proc in psutil.process_iter(): # iterate processes
            if proc.name() == PROCNAME: # if league of legends is open, kill it
                proc.kill() 
                messagebox.showinfo(title="Stop playing League of Legends!", message="Go outside!")
        sleep(10)

if __name__ == '__main__':
    main()