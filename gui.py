import tkinter as tk
window = tk.Tk()
window.title("My first GUI")
window.geometry('500x300')
hello = tk.Label(text="Hello CS 222")
clickMe = tk.Button(text="Click me", width=10, height=3)
hello.pack()
clickMe.pack()
window.mainloop()