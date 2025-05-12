#não soube fazer, pedi ao chatgpt fazer com tkinter pq era o que o professor Fábio ou Ivo usava
m
import tkinter as tk
from tkinter import ttk, messagebox

def cadastrar_produto():
    tipo = tipo_var.get()
    modelo = entry_modelo.get()
    cor = entry_cor.get()
    preco = float(entry_preco.get())
    categoria = Categoria(1, entry_categoria.get())

    if tipo == "Desktop":
        potencia = entry_extra.get()
        desktop = Desktop(modelo, cor, preco, categoria, potencia)
        messagebox.showinfo("Cadastro", desktop.getInformacoes())
        desktop.cadastrar()

    elif tipo == "Notebook":
        bateria = entry_extra.get()
        notebook = Notebook(modelo, cor, preco, categoria, bateria)
        messagebox.showinfo("Cadastro", notebook.getInformacoes())
        notebook.cadastrar()

janela = tk.Tk()
janela.title("Cadastro de Produtos")

tk.Label(janela, text="Modelo:").grid(row=0, column=0)
entry_modelo = tk.Entry(janela)
entry_modelo.grid(row=0, column=1)

tk.Label(janela, text="Cor:").grid(row=1, column=0)
entry_cor = tk.Entry(janela)
entry_cor.grid(row=1, column=1)

tk.Label(janela, text="Preço:").grid(row=2, column=0)
entry_preco = tk.Entry(janela)
entry_preco.grid(row=2, column=1)

tk.Label(janela, text="Categoria:").grid(row=3, column=0)
entry_categoria = tk.Entry(janela)
entry_categoria.grid(row=3, column=1)

tk.Label(janela, text="Tipo:").grid(row=4, column=0)
tipo_var = tk.StringVar()
tipo_menu = ttk.Combobox(janela, textvariable=tipo_var)
tipo_menu['values'] = ("Desktop", "Notebook")
tipo_menu.grid(row=4, column=1)

tk.Label(janela, text="Potência (W) ou Bateria (h):").grid(row=5, column=0)
entry_extra = tk.Entry(janela)
entry_extra.grid(row=5, column=1)

btn = tk.Button(janela, text="Cadastrar", command=cadastrar_produto)
btn.grid(row=6, columnspan=2)

janela.mainloop()
