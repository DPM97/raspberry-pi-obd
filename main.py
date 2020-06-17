import obd
from time import sleep
import tkinter as tk
import random

class gauge:
    def __init__(self, master):
        self.connection = obd.OBD()
        self.boost = tk.StringVar()
        self.boost.set("")
        self.master = master
        master.configure(bg="black")
        boostLabel = tk.Label(master, text="Boost", bg="black", fg="white", font="none 70 bold")
        boostLabel.place(relx=.5, rely=.4, anchor="center")
        boost = tk.Label(master, bg="black", fg="white", font="none 50 bold", textvariable=self.boost)
        boost.place(relx=.5, rely=.5, anchor="center")
        self.fetchBoost()

    def fetchBoost(self):
        c = obd.commands[6][85]
        if (self.connection.status() == "Not Connected"):
            self.boost.set("")
        else:
            r = self.connection.query(c)
            self.boost.set(str(random.randint(-15,-13)))

        self.master.after(200, self.fetchBoost)




root = tk.Tk()
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)
app=gauge(root)
root.mainloop()

