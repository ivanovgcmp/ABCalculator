# A/B calculator

import tkinter as tk

# Creating function close program
def do_Close():
	root.destroy()

# Creating main window
root = tk.Tk()
root.geometry("280x300")
root.title("A/B calculator")

# Adding a header label
lblTitle = tk.Label(text = 'A/B calculator', font = ('Helvetica', 14, 'bold'), fg = '#0000cc')
lblTitle.place(x=70, y=20)

# Adding the Calculate button
btnProcess = tk.Button(root, text = 'Calculation', font = ('Helvetica', 10, 'bold'))
btnProcess.place(x=25, y=250, width=90, height=30)


# Adding a Close button
btnClose = tk.Button(root, text="Close", font = ('Helvetica', 10, 'bold'), command=do_Close)
btnClose.place(x=160, y=250, width=90, height=30)

# Start mainloop
root.mainloop()
