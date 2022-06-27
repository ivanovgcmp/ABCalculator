# A/B calculator

import tkinter as tk
from tkinter import messagebox as mb
import os
import math
from scipy.stats import norm

# Creating function close program
def do_Close():
    root.destroy()

# Percentage formatting function
def num_percent(num):
    return "{:.2f}".format(num*100).rjust(10) + '%'

# Function reading data from input fields
def do_processing():

    n1 = int(entVisit1.get())
    c1 = int(entConvers1.get())
    n2 = int(entVisit2.get())
    c2 = int(entConvers2.get())
    # Checking data from input fields
    if n1<=0 or n2<=0:
        mb.showerror(title='Error when dividing zero', message='Incorrect number of visitors')
        return
    # Opening the Results window
    popup_window(n1, c1, n2, c2)

# Function of calling the results window
def popup_window(n1, c1, n2, c2):
    window = tk.Toplevel()
    window.geometry("500x500")
    window.title("A/B result")

    # Adding a text output window
    txtOutput = tk.Text(window, font = ('Courier New', 10, 'bold'))
    txtOutput.place(x=15, y=115, width=470, height=300)

    # Adding headers
    txtOutput.insert(tk.END, '                          Control          Test'  + os.linesep)
    txtOutput.insert(tk.END, '                          group            group' + os.linesep)
    txtOutput.insert(tk.END, '------------------------------------------------------' + os.linesep)

    # Adding conversion output and standard deviation
    p1 = c1/n1
    p2 = c2/n2
    txtOutput.insert(tk.END, 'Conversion            ' + num_percent(p1)
        + '    ' + num_percent(p2) + os.linesep)

    sigma1 = math.sqrt(p1*(1-p1)/n1)
    sigma2 = math.sqrt(p2*(1-p2)/n2)
    txtOutput.insert(tk.END, 'Standard deviation    ' + num_percent(sigma1)
        + '    ' + num_percent(sigma2) + os.linesep)
    txtOutput.insert(tk.END, '------------------------------------------------------' + os.linesep)

    # Adding possible scatter output fields
    z1 = 1.96
    lower1_95 = p1-z1*sigma1
    if lower1_95 < 0:
        lower1_95 = 0
    upper1_95 = p1+z1*sigma1

    if upper1_95 > 1:
        upper1_95 = 1
    lower2_95 = p2-z1*sigma2

    if lower2_95 < 0:
        lower2_95 = 0
    upper2_95 = p2+z1*sigma2

    if upper2_95 > 1:
        upper2_95 = 1

    txtOutput.insert(tk.END, '95% Possible dispersion      ' + os.linesep)
    txtOutput.insert(tk.END, '                   from   '        + num_percent(lower1_95)
        + '     ' + num_percent(lower2_95) + os.linesep)
    txtOutput.insert(tk.END, '                     to   '        + num_percent(upper1_95)
        + '     ' + num_percent(upper2_95) + os.linesep)
    txtOutput.insert(tk.END, '------------------------------------------------------' + os.linesep)

    z2 = 2.575
    lower1_99 = p1-z2*sigma1
    if lower1_99 < 0:
        lower1_99 = 0
    upper1_99 = p1+z2*sigma1

    if upper1_99 > 1:
        upper1_99 = 1

    lower2_99 = p2-z2*sigma2
    if lower2_99 < 0:
        lower2_99 = 0
    upper2_99 = p2+z2*sigma2

    if upper2_99 > 1:
        upper2_99 = 1

    txtOutput.insert(tk.END, '99% Possible dispersion      ' + os.linesep)
    txtOutput.insert(tk.END, '                   from   ' + num_percent(lower1_99)
        + '     ' + num_percent(lower2_99) + os.linesep)
    txtOutput.insert(tk.END, '                     to   ' + num_percent(upper1_99)
        + '     ' + num_percent(upper2_99) + os.linesep)
    txtOutput.insert(tk.END, '------------------------------------------------------' + os.linesep)

    # Calculation value Z & P
    z_score = (p2-p1)/math.sqrt(sigma1*sigma1+sigma2*sigma2)
    txtOutput.insert(tk.END, 'Z = ' + "{:.7f}".format(z_score) + os.linesep)

    p_value = norm.sf(x=z_score, loc=0, scale=1)
    txtOutput.insert(tk.END, 'P = ' + "{:.7f}".format(p_value) + os.linesep)

    # Adding estimation results
    confidence_95 = False
    if p_value < 0.025 or p_value > 0.975:
        confidence_95 = True

    confidence_99 = False
    if p_value < 0.005 or p_value > 0.995:
        confidence_99 = True

    lblComment95 = tk.Label(window, text = "95% confidence: ", font = ('Helvetica', 10, 'bold'))
    lblComment95.place(x=25, y=25)

    if confidence_95:
        lblResult95 = tk.Label(window, text = 'Yes', font = ('Helvetica', 12, 'bold'), fg = '#008800')
        lblResult95.place(x=160, y=25)
    else:
        lblResult95 = tk.Label(window, text = 'No', font = ('Helvetica', 12, 'bold'), fg = '#ff0000')
        lblResult95.place(x=160, y=25)

    lblComment99 = tk.Label(window, text = "99% confidence: ", font = ('Helvetica', 10, 'bold'))
    lblComment99.place(x=25, y=65)

    if confidence_99:
        lblResult99 = tk.Label(window, text = 'Yes', font = ('Helvetica', 12, 'bold'), fg = '#008800')
        lblResult99.place(x=160, y=65)
    else:
        lblResult99 = tk.Label(window, text = 'No', font = ('Helvetica', 12, 'bold'), fg = '#ff0000')
        lblResult99.place(x=160, y=65)

    # Adding button close window
    btnClosePopup = tk.Button(window, text="Close", font = ('Helvetica', 10, 'bold'), command=window.destroy)
    btnClosePopup.place(x=200, y=450, width=90, height=30)

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
entVisit1.insert(tk.END, '255')

lblConvers1 = tk.Label(text = 'Conversion', font = ('Helvetica', 10, 'bold'))
lblConvers1.place(x=25, y=115)

entConvers1 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')
entConvers1.place(x=115, y=115, width=90, height=20)
entConvers1.insert(tk.END, '26')

# Adding a Test group header label
lblTitle = tk.Label(text = 'Test group', font = ('Helvetica', 12, 'bold'), fg = '#0000cc')
lblTitle.place(x=25, y=145)

# Adding Test Group input fields
lblVisit2 = tk.Label(text = 'Visitors', font = ('Helvetica', 10, 'bold'))
lblVisit2.place(x=25, y=170)

entVisit2 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')
entVisit2.place(x=115, y=170, width=90, height=20)
entVisit2.insert(tk.END, '235')

lblConvers2 = tk.Label(text = 'Conversion', font = ('Helvetica', 10, 'bold'))
lblConvers2.place(x=25, y=200)

entConvers2 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')
entConvers2.place(x=115, y=200, width=90, height=20)
entConvers2.insert(tk.END, '18')

# Adding the Calculate button
btnProcess = tk.Button(root, text = 'Calculation', font = ('Helvetica', 10, 'bold'), command=do_processing)
btnProcess.place(x=25, y=250, width=90, height=30)


# Adding a Close button
btnClose = tk.Button(root, text="Close", font = ('Helvetica', 10, 'bold'), command=do_Close)
btnClose.place(x=160, y=250, width=90, height=30)

# Start mainloop
root.mainloop()
