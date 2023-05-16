import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
destinolabel = tk.Label(root, text="Seleccione su Destino")
destinolabel.grid(row=0,column=1)

destino = ttk.Combobox(root, values=("Madrid", "Miami", "Rio de Janeiro", "Montevideo"))
destino.set("Montevideo")
destino.grid(row=1,column=1,padx=10,pady=10)


pasajeslabel = tk.Label(root, text="Seleccione Pasajeros")
pasajeslabel.grid(row=0,column=2)
pasajes = ttk.Combobox(root, values=("1", "2", "3", "4","5"))
pasajes.set("2")
pasajes.grid(row=1,column=2,padx=10,pady=10)



def precio():
    valdicc={"Madrid":650, "Miami":450, "Rio de Janeiro":200, "Montevideo":100}
    d = str(destino.get())
    p = int(pasajes.get())
    preciofinal = valdicc[d]*p
    ttk.Label(root,text = f"valor por {p} pasajes" ).grid(row=3,column=1)
    ttk.Label(root,text = preciofinal ).grid(row=3,column=2,padx=10,pady=10)

tk.Button(root, text="Consultar", fg = "white", bg = "silver", font = "Helvetica 20 bold italic",command=precio).grid(row=3,column=0) 

root.mainloop()
