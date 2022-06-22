# A/B calculator

import tkinter as tk

# Creating function close program
def do_Close():
	root.destroy()

def do_processing():
	# Reading data from input fields
	n1 = int(entVisit1.get())
	c1 = int(entConvers1.get())
	n2 = int(entVisit2.get())
	c2 = int(entConvers2.get())
	
	popup_window(n1, c1, n2, c2)

def popup_window(n1, c1, n2, c2):
	window = tk.Toplevel()
	window.geometry("280x300")
	window.title("A/B result")
	
	# Adding button Close window
	btnClosePopup = tk.Button(window, text="Close", font = ('Helvetica', 10, 'bold'), command=window.destroy)
	btnClosePopup.place(x=160, y=250, width=90, height=30)
	
	# Focus to the created window 
	window.focus_force()

# Creating main window
root = tk.Tk()
root.geometry("280x300")
root.title("A/B calculator")

# Adding a title form
lblTitle = tk.Label(text = 'A/B calculator', font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=70, y=20)

# Adding a Control group header label 
lblTitle = tk.Label(text = 'Control group', font = ('Helvetica', 12, 'bold'), fg = '#0000cc')
lblTitle.place(x=25, y=55)

# Adding Control Group input fields
lblVisit1 = tk.Label(text = 'Visitors', font = ('Helvetica', 10, 'bold'))
lblVisit1.place(x=25, y=85)

entVisit1 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')
entVisit1.place(x=115, y=85, width=90, height=20)
entVisit1.insert(tk.END, '0')

lblConvers1 = tk.Label(text = 'Conversion', font = ('Helvetica', 10, 'bold'))
lblConvers1.place(x=25, y=115)

entConvers1 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')
entConvers1.place(x=115, y=115, width=90, height=20)
entConvers1.insert(tk.END, '0')

# Adding a Test group header label 
lblTitle = tk.Label(text = 'Test group', font = ('Helvetica', 12, 'bold'), fg = '#0000cc')
lblTitle.place(x=25, y=145)

# Adding Test Group input fields
lblVisit2 = tk.Label(text = 'Visitors', font = ('Helvetica', 10, 'bold'))
lblVisit2.place(x=25, y=170)

entVisit2 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')
entVisit2.place(x=115, y=170, width=90, height=20)
entVisit2.insert(tk.END, '0')

lblConvers2 = tk.Label(text = 'Conversion', font = ('Helvetica', 10, 'bold'))
lblConvers2.place(x=25, y=200)

entConvers2 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')
entConvers2.place(x=115, y=200, width=90, height=20)
entConvers2.insert(tk.END, '0')

# Adding the Calculate button
btnProcess = tk.Button(root, text = 'Calculation', font = ('Helvetica', 10, 'bold'), command=do_processing)
btnProcess.place(x=25, y=250, width=90, height=30)


# Adding a Close button
btnClose = tk.Button(root, text="Close", font = ('Helvetica', 10, 'bold'), command=do_Close)
btnClose.place(x=160, y=250, width=90, height=30)

# Start mainloop
root.mainloop()
