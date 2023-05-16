import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from datetime import date

root = tk.Tk()
root.title("EDAD")
labdia = ttk.Label(root,text="Dia").grid(row=0,column=0,padx=10,pady=10)
dia =ttk.Entry(root)
dia.grid(row=0,column=1)

labmes = ttk.Label(root,text="Mes").grid(row=1,column=0,padx=10,pady=10)
mes = ttk.Combobox(root, values=("Enero", "Febrero", "Marzo", "Abril", "Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"))
mes.set("Enero")
mes.grid(row=1,column=1)

labyear = ttk.Label(root,text="Anio").grid(row=2,column=0,padx=10,pady=10)
year =ttk.Entry(root)
year.grid(row=2,column=1)

def escribir():
    dicdias={"Enero":(1,31), "Febrero":(2,28), "Marzo":(3,31), "Abril":(4,30),"Mayo":(5,31),"Junio":(6,30),"Julio":(7,31),"Agosto":(8,31),"Septiembre":(9,30),"Octubre":(10,31),"Noviembre":(11,30),"Diciembre":(12,31)}
    try:
        d = int(dia.get())
        m = str(mes.get())
        y = int(year.get())
        today = date.today()
        cumplea=date(y,dicdias[m][0],d)
        if d > dicdias[m][1] or len(str(y)) != 4  or y > today.year:
            raise ("len error")  
        edad = today.year - cumplea.year - ((today.month, today.day) < (cumplea.month, cumplea.day))  
    except:
        tk.messagebox.showwarning(title="Datos No validos", message="Corrobore dia (DD) y anio (YYYY)")
    ttk.Label(root,text = "Edad: " ).grid(row=3,column=0)
    ttk.Label(root,text = edad ).grid(row=3,column=1,padx=10,pady=10)

tk.Button(root, text="Submit", fg = "black", bg = "gold", font = "Helvetica 20 bold italic",command = escribir).grid(row=3,column=0) 

root.mainloop()

#Ejemplo by Lean