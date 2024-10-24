import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.roupabanco import Roupabanco
from backend.FornecedorBanco import FornecedorBanco

def comando():
    root = tk.Tk()
    root.geometry("600x400")
    root.title("Tabela de Produtos")

    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    tree = ttk.Treeview(frame, columns=("peca", "valor", "marca", "tamanho", "codigo"), show="headings")

    tree.heading("peca", text="Peca")
    tree.heading("valor", text="Valor")
    tree.heading("marca", text="Marca")
    tree.heading("tamanho", text="Tamanho")
    tree.heading("codigo", text="Codigo")


    rb=Roupabanco()
    dados=rb.get_all_roupa()

    for item in dados:
        if item.ativo==True:
            tree.insert("", tk.END, values=(item.peca,item.valor,item.marca,item.tamanho,item.codigo))

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tree.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

def adicionar_produto():
    janela=tk.Tk()
    janela.geometry("600x400")

    global entrypeca
    global entryvalor
    global entrymarca
    global entrytamanho
    global entryfornecedor

    peca=tk.Label(janela,text="Peça")
    peca.pack()
    entrypeca=tk.Entry(janela)
    entrypeca.pack()

    valor=tk.Label(janela,text="valor")
    valor.pack()
    entryvalor=tk.Entry(janela)
    entryvalor.pack()

    marca=tk.Label(janela,text="marca")
    marca.pack()
    entrymarca=tk.Entry(janela)
    entrymarca.pack()

    tamanho=tk.Label(janela,text="tamanho")
    tamanho.pack()
    entrytamanho=tk.Entry(janela)
    entrytamanho.pack()

    fornecedor=tk.Label(janela,text="digite o codigo do fornecedor")
    fornecedor.pack()
    entryfornecedor=tk.Entry(janela)
    entryfornecedor.pack()

    botao=tk.Button(janela,text="salvar novo produto",command=criar)
    botao.pack(pady=5)
    janela.mainloop()
def criar():
    global entrypeca
    global entryvalor
    global entrymarca
    global entrytamanho
    global entryfornecedor

    peca=entrypeca.get()
    valor=entryvalor.get()
    marca=entrymarca.get()
    tamanho=entrytamanho.get()
    codigoforn=entryfornecedor.get()
    ativo=True

    rb=Roupabanco()
    try:
        add=rb.add_roupa(peca,valor,marca,tamanho,ativo)
        messagebox.showinfo('certo','adicionada com sucesso')
    except:
        messagebox.showerror('erro','tente novamente')

def deletar():
    global entry_cod
    janela= tk.Tk()
    janela.geometry("600x400")
    label=tk.Label(janela,text="digite o codigo da roupa que você quer vender:")
    label.pack(pady=5)

    entry_cod=tk.Entry(janela)
    entry_cod.pack()

    deletar=tk.Button(janela,text="vender",command=vender)
    deletar.pack(pady=5)
def vender():
    global entry_cod
    cod=entry_cod.get()
    rb=Roupabanco()
    try:
        exc=rb.delete_roupa(cod)
        messagebox.showinfo("certo","vendido com sucesso")
    except:
        messagebox.showerror("errado","nao foi possivel realizar a venda,confira ")
    
def atualizaritem():
    global entry_peca
    global entry_valor
    global entry_marca
    global entry_tamanho
    global entry_cod

    janela=tk.Tk ()
    janela.title("atualizar")
    label_codigo=tk.Label(janela,text="Digite o codigo do peça que você quer atualizar ")
    label_codigo.pack()
    janela.geometry("600x400")

    entry_cod=tk.Entry(janela)
    entry_cod.pack()

    label_peca=tk.Label(janela,text="peca")
    label_peca.pack()

    entry_peca=tk.Entry(janela)
    entry_peca.pack()

    label_valor=tk.Label(janela,text="valor")
    label_valor.pack()

    entry_valor=tk.Entry(janela)
    entry_valor.pack()

    label_marca=tk.Label(janela,text="marca")
    label_marca.pack()

    entry_marca=tk.Entry(janela)
    entry_marca.pack()

    label_Tamanho=tk.Label(janela,text="tamanho")
    label_Tamanho.pack()

    entry_tamanho=tk.Entry(janela)
    entry_tamanho.pack()

    botao=tk.Button (janela,text="atualizar",command=atualizari)
    botao.pack()

    janela.mainloop()
def atualizari():
    global entry_peca
    global entry_valor
    global entry_marca
    global entry_tamanho
    global entry_cod

    peca= entry_peca.get()
    valor= entry_valor.get()
    marca= entry_marca.get()
    tamanho= entry_tamanho.get()
    cod=entry_cod.get()

    tb=Roupabanco()
    try:
        atualizari=tb.atualizar(peca,valor,marca,tamanho,cod)
        messagebox.showinfo("atualizado", " item atualizado com sucesso")
    except:
        messagebox.showerror("nao foi possivel atualizar", "tente novamente")

def fornecedores():
    root = tk.Tk()
    root.geometry("600x400")
    root.title("Tabela de Fornecedores")

    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    tree = ttk.Treeview(frame, columns=("nome", "codigo_produto", "codigo_fornecedor"), show="headings")

    tree.heading("nome", text="Nome")
    tree.heading("codigo_produto", text="Código Produto")
    tree.heading("codigo_fornecedor", text="Código Fornecedor")

    fb = FornecedorBanco()
    dados = fb.get_all_fornecedores()

    for item in dados:
        tree.insert("", tk.END, values=(item.nomeforn,item.codigoprod,item.codigoforn))

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tree.pack(fill=tk.BOTH, expand=True)

    root.mainloop() 

def run():
    janela = tk.Tk()
    janela.title('')
    janela.geometry("500x300")

    botao = tk.Button(janela, text='Ver Produtos', command=comando)
    botao.pack(pady=4)

    botao_deletar=tk.Button(janela,text='vender',command=deletar)
    botao_deletar.pack()

    btn_adicionar = tk.Button(janela, text="Adicionar Produto", command=adicionar_produto)
    btn_adicionar.pack(pady=10)

    atualizar=tk.Button (janela, text=" atualizar item", command=atualizaritem)
    atualizar.pack()

    botaoparafornecedores=tk.Button(janela,text="ver dados do fornecedor",command=fornecedores)
    botaoparafornecedores.pack()
    janela.mainloop()


# CREATE TABLE guardaroupa (
# peca varchar (20),
# valor varchar (20),
# marca varchar (20),
# tamanho varchar (20),
# fabrica varchar (20),
# codigo serial primary key
# )

# CREATE TABLE fornecedor (
# nomeforn varchar (20),
# codigoprod int,
# codigoforn serial primary key
# )

# CREATE TABLE usuario (
# nome varchar(50),
# senha varchar (50),
# codigo serial primary key
# )