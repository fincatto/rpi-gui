import sys
import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.config(cursor="none")
        self.title("Imagem Filmes")
        self.bind('<Escape>', sys.exit)
        self.attributes("-fullscreen", True)

        # label aleatorio
        lbl = tk.Label(self, text="Oi mundo!")
        lbl.grid(sticky="W", column=0, row=0)

        # barra de progresso aleatoria
        pb = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        pb.grid(sticky="W", column=0, row=1)
        pb["maximum"] = 100
        pb["value"] = 10


if __name__ == '__main__':
    window = MainWindow()
    window.mainloop()
