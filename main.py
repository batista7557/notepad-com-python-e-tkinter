import tkinter

window = tkinter.Tk()
window.title("Notepad")
window.geometry("1280x720")

frame = tkinter.Frame(window, height=30)
frame.pack(fill="x")

font_text = tkinter.Label(frame, text="Fonte: ")
font_text.pack(side="left")

spin_font = tkinter.Spinbox(frame, values=("Arial", "Verdana"))
spin_font.pack(side="left")

font_size = tkinter.Label(frame, text=" Tamanho da fonte: ")
font_size.pack(side="left")

spin_size = tkinter.Spinbox(frame, from_=0, to=60)
spin_size.pack(side="left")

def UpdateFont():
    size = spin_size.get()
    font = spin_font.get()
    text_area.config(font="{} {}".format(font, size))

button_update = tkinter.Button(frame, text="Atualizar", command=UpdateFont)
button_update.pack(side="left")

text_area = tkinter.Text(window, font="Arial 20 bold", width=1280, height=720)
text_area.pack()

main_menu = tkinter.Menu(window)

def NewFile():
    text_area.delete(1.0, "end")

def Save():
    container = text_area.get(1.0, "end")
    file = open("notepad.txt", "w")
    file.write(container)
    file.close()

def Open():
    file = open("notepad.txt", "r")
    container = file.read()
    text_area.insert(1.0, container)

file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label="New", command=NewFile)
file_menu.add_command(label="Save", command=Save)
file_menu.add_command(label="Open", command=Open)
file_menu.add_command(label="Exit", command=window.quit)

main_menu.add_cascade(label="File", menu=file_menu)
window.config(menu=main_menu)
window.mainloop()

