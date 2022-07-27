# Ali Jafarbeglou - Mile to Km Convertor - OOP tkinter
import tkinter
from tkinter import *

window = Tk()
window.title("Mile to Km Convertor")
window.minsize(250, 150)
window.maxsize(250, 150)
window.config(padx=20 ,pady=20)
# window.configure(bg="gray")

input = tkinter.Entry(width=8)
input.grid(column=1, row=0)

mile_label = tkinter.Label(text="Miles")
mile_label.grid(column=2, row=0)

label_2 = tkinter.Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = tkinter.Label(text="0")
label_3.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)


# Button
def mile_to_km():
    mile = float(input.get())
    res = round(mile * 1.609)
    label_3.config(text=res)


cal_button = tkinter.Button(text="Calculate", command=mile_to_km)
cal_button.grid(column=1, row=2)


window.mainloop()










