import tkinter as tk
from tkinter import messagebox

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def realizar_operacion():
    try:
        expression = entry.get()
        result = str(eval(expression))  # Utiliza la función eval() con precaución
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Ha ocurrido un error en la operación.")

def salir():
    root.destroy()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora con Teclado")

# Estilos
root.configure(bg='#f7f7f7')
fuente = ('Arial', 12)

# Entry para mostrar los números y resultados
entry = tk.Entry(root, font=fuente, width=15, borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones para los números y operaciones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0
for boton in botones:
    command = lambda x=boton: click_button(x) if x not in {'C', '='} else clear_entry() if x == 'C' else realizar_operacion()
    if boton == 'C':
        tk.Button(root, text=boton, padx=20, pady=20, bg="#f44336", fg='white', font=fuente, command=command).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=boton, padx=20, pady=20, bg="#4CAF50", fg='white', font=fuente, command=command).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

salir_button = tk.Button(root, text="Salir", command=salir, font=fuente, bg='#f44336', fg='white', padx=20, pady=20)
salir_button.grid(row=row_val, column=0, columnspan=4)

root.mainloop()