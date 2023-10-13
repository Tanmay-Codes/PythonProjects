from tkinter import *

window = Tk()
window.title("Miles to km calculator")
window.minsize(width=400, height=400)
window.config(padx=100, pady=100)


def milestokm():
    miles = float(input_label.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


input_label = Entry()
input_label.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=milestokm)
calculate_button.grid(column=1, row=3)

window.mainloop()
