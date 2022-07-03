import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def program_expired():
    app_date = datetime(year=2023,month=5,day=1) #setup a datetime object
    now = datetime.now()
    if (now-app_date).days >=5: #change to 30
        messagebox.showerror("Error","Your tool had expired")
    else:
        main()

def main():
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.geometry("550x300")
    root.title("Tool")
    root.mainloop()

program_expired()