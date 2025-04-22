from tkinter import *

window=Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

# label

mile_label=Label(text="Miles")
km_label=Label(text="Km")
km_value=Label(text="0")

equal_label=Label(text="is equal to")

mile_label.grid(column=3, row=1)
km_label.grid(column=3,row=2)
equal_label.grid(column=1,row=2)
km_value.grid(column=2,row=2)

input=Entry(width=10)
input.grid(column=2,row=1)

def action():
    input_num=float(input.get())
    value=input_num*1.609
    km_value.config(text=f"{value}")

button = Button(text="Calculate", command=action)
button.grid(column=2,row=3)


window.mainloop()