from tkinter import*
def pesquisar():
    global dolar, euro, bitcoin, taxas
    if entry.get().lower() == "dolar":
        label = Label(root, text=str(dolar), font=("Arial", 24))
        label.pack()
    elif entry.get().lower() == "euro":
        label = Label(root, text=str(euro), font=("Arial", 24))
        label.pack()
    elif entry.get().lower() == "bitcoin":
        label = Label(root, text=str(bitcoin), font=("Arial", 24))
        label.pack()
    elif entry.get().lower() == "taxs":
        label = Label(root, text=str(taxs), font=("Arial", 24))
        label.pack()
    else:
        label = Label(root, text="erro, this doesn't exist", font=("Arial", 24))
        label.pack()
    label.after(2000, label.destroy)

dolar = "5.25"
euro = "5.90"
bitcoin = "134000.00"
taxs = "0.60"

root=Tk()
root.title("countlab")
root.config(background="#303030")

entry = Entry(root, font=("Arial", 24))
entry.pack(pady=20)
button = Button(root, text="Pesquisar", font=("Arial", 24), command=pesquisar)
button.pack()

root.mainloop()