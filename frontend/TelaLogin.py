import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.UsuarioBanco import UsuarioBanco 
from frontend.TelaHome import run

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    objeto = UsuarioBanco()
    usuario = objeto.get_usuario_pelo_nome(username)

    if usuario is not None and usuario.senha == password:
        run()
    else:
        messagebox.showerror("Login", "Não é possível se conectar, confira se o nome do usuário e sua senha estão corretos")

root = tk.Tk()
root.title("Tela de Login")
root.geometry("500x300")

label_username = tk.Label(root, text="vendedora:")
label_username.pack(pady=5)

entry_username = tk.Entry(root) 
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Senha:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

button_login = tk.Button(root, text="acessar vendas", command=login)
button_login.pack(pady=20)

root.mainloop()