import tkinter

window = tkinter.Tk()
window.title("Notepad")
window.geometry("1280x720")

text_area = tkinter.Text(window, font="Arial 20 bold", width=1280, height=720)
text_area.pack()

main_menu = tkinter.Menu(window)

def NewFile():
    print("Crie um novo arquivo")

def Save():
    print("Arquivo salvo")

def Save_as():
    print("Salvar como...")

file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label="New", command=NewFile)
file_menu.add_command(label="Save", command=Save)
file_menu.add_command(label="Save as...", command=Save_as)
file_menu.add_command(label="Exit", command=window.quit)

main_menu.add_cascade(label="File", menu=file_menu)
window.config(menu=main_menu)
window.mainloop()

