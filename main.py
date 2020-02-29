import sys
import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk()
    window.config(cursor="none")
    window.title("Imagem Filmes")
    window.bind('<Escape>', sys.exit)
    window.attributes("-fullscreen", True)
    lbl = tk.Label(window, text="Oi mundo!")
    lbl.grid(column=0, row=0)
    window.mainloop()
