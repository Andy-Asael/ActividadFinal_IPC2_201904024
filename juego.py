from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Totito')
click = True
count = 0

def getganador():
	global ganador
	ganador = False

	if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X":
		b1.config(bg="blue")
		b2.config(bg="blue")
		b3.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J1 Gana!!!")
		disable_all_buttons()
	elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]  == "X":
		b4.config(bg="blue")
		b5.config(bg="blue")
		b6.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J1 Gana!!!")
		disable_all_buttons()

	elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]  == "X":
		b7.config(bg="blue")
		b8.config(bg="blue")
		b9.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J1 Gana!!!")
		disable_all_buttons()

	elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]  == "X":
		b1.config(bg="blue")
		b4.config(bg="blue")
		b7.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J1 Gana!!!")
		disable_all_buttons()

	elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]  == "X":
		b2.config(bg="blue")
		b5.config(bg="blue")
		b8.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J1 Gana!!!")
		disable_all_buttons()

	elif b3["text"] == "X" and b6["text"] == "X" and b9["text"]  == "X":
		b3.config(bg="blue")
		b6.config(bg="blue")
		b9.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J1 Gana!!!")
		disable_all_buttons()

	elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X":
		b1.config(bg="blue")
		b5.config(bg="blue")
		b9.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J1 Gana!!!")
		disable_all_buttons()

	elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]  == "X":
		b3.config(bg="blue")
		b5.config(bg="blue")
		b7.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J1 Gana!!!")
		disable_all_buttons()

	elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
		b1.config(bg="blue")
		b2.config(bg="blue")
		b3.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J2 Gana!!!")
		disable_all_buttons()
	elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]  == "O":
		b4.config(bg="blue")
		b5.config(bg="blue")
		b6.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J2 Gana!!!")
		disable_all_buttons()

	elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]  == "O":
		b7.config(bg="blue")
		b8.config(bg="blue")
		b9.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J2 Gana!!!")
		disable_all_buttons()

	elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]  == "O":
		b1.config(bg="blue")
		b4.config(bg="blue")
		b7.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J2 Gana!!!")
		disable_all_buttons()

	elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]  == "O":
		b2.config(bg="blue")
		b5.config(bg="blue")
		b8.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J2 Gana!!!")
		disable_all_buttons()

	elif b3["text"] == "O" and b6["text"] == "O" and b9["text"]  == "O":
		b3.config(bg="blue")
		b6.config(bg="blue")
		b9.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J2 Gana!!!")
		disable_all_buttons()

	elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O":
		b1.config(bg="blue")
		b5.config(bg="blue")
		b9.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J2 Gana!!!")
		disable_all_buttons()

	elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]  == "O":
		b3.config(bg="blue")
		b5.config(bg="blue")
		b7.config(bg="blue")
		ganador = True
		messagebox.showinfo("Totito", "J2 Gana!!!")
		disable_all_buttons()

	if count == 9 and ganador == False:
		messagebox.showinfo("Totito", "Empate")
		disable_all_buttons()
				

def b_click(b):
	global click, count

	if b["text"] == " " and click == True:
		b["text"] = "X"
		click = False
		count += 1
		getganador()
	elif b["text"] == " " and click == False:
		b["text"] = "O"
		click = True
		count += 1
		getganador()



def crear():
	global b1, b2, b3, b4, b5, b6, b7, b8, b9
	global click, count
	click = True
	count = 0

	b1 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b1))
	b2 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b2))
	b3 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b3))

	b4 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b4))
	b5 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b5))
	b6 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b6))

	b7 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b7))
	b8 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b8))
	b9 = Button(root, text=" ", height=3, width=6, command=lambda: b_click(b9))

	b1.grid(row=0, column=0)
	b2.grid(row=0, column=1)
	b3.grid(row=0, column=2)

	b4.grid(row=1, column=0)
	b5.grid(row=1, column=1)
	b6.grid(row=1, column=2)

	b7.grid(row=2, column=0)
	b8.grid(row=2, column=1)
	b9.grid(row=2, column=2)

crear()
root.mainloop()