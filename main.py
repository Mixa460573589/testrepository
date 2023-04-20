from tkinter import *
def calc():
    if output_entry.get()!='':
        output_entry.delete(0, END)
        output_entry.insert(0, eval(input_entry.get()))
    else:
        output_entry.insert(0, eval(input_entry.get()))
window = Tk()
window.title("Вычисление выражений")
window.geometry('400x300')
label1 = Label(
    text="Выражение: "
)
label1.grid(row=1, column=1)
label2 = Label(
    text="Результат: "
)
label2.grid(row=1, column=3)
input_entry = Entry(
)
input_entry.grid(row=2, column=1)
output_entry = Entry(
)
output_entry.grid(row=2, column=3)
cal_btn = Button(
    text='->',
    command = calc)
cal_btn.grid(row=2, column=2)
window.mainloop()