import tkinter

window = tkinter.Tk()
window.title("Notepad")
window.geometry("1280x720")

text_area = tkinter.Text(window, font="Arial 20 bold")
text_area.pack()

main_menu = tkinter.Menu(window)

file_menu = tkinter.Menu(main_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save as...")

main_menu.add_cascade(label="File", menu=file_menu)
window.config(menu=main_menu)
window.mainloop()