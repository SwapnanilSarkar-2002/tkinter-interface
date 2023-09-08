import tkinter as tk
window=tk.Tk()
window.geometry("600x400")
window.title("ECE")
def click_me():
    l1=tk.Label(window,text="Hi", font = ('calibre',10,'bold'))
    l1.pack()
bt=tk.Button(window,text="CLICK", command=click_me) 
bt.pack()
window.mainloop()  
