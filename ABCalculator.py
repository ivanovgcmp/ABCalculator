# A/B calculator

import tkinter as tk

# Creating function close program
def do_Close():
	root.destroy()

# Creating main window
root = tk.Tk()
root.geometry("280x300")
root.title("A/B calculator")

# Adding a title form
lblTitle = tk.Label(text = 'A/B calculator', font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=70, y=20)

# Adding a control group header label 
lblTitle = tk.Label(text = 'Control group', font = ('Helvetica', 12, 'bold'), fg = '#0000cc')
lblTitle.place(x=25, y=55)

# Adding Control Group input fields
lblVisit1 = tk.Label(text = 'Visitors', font = ('Helvetica', 10, 'bold'))
lblVisit1.place(x=25, y=85)

entVisit1 = tk.Entry(font = ('Helvetica', 10, 'bold'))
entVisit1.place(x=115, y=85, width=90, height=20)

lblConvers = tk.Label(text = 'Conversion', font = ('Helvetica', 10, 'bold'))
lblConvers.place(x=25, y=115)

entConvers = tk.Entry(font = ('Helvetica', 10, 'bold'))
entConvers.place(x=115, y=115, width=90, height=20)


# Adding the Calculate button
btnProcess = tk.Button(root, text = 'Calculation', font = ('Helvetica', 10, 'bold'))
btnProcess.place(x=25, y=250, width=90, height=30)


# Adding a Close button
btnClose = tk.Button(root, text="Close", font = ('Helvetica', 10, 'bold'), command=do_Close)
btnClose.place(x=160, y=250, width=90, height=30)

# Start mainloop
root.mainloop()
