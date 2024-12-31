import tkinter as tk
from tkinter import messagebox
import random
import string

def gerar_senha():
    try:
        qtd_caracteres_senha = int(entry_qtd.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para a quantidade de caracteres.")
        return

    incluir_numero = var_numero.get()
    incluir_letra_minuscula = var_minuscula.get()
    incluir_letra_maiscula = var_maiscula.get()
    incluir_simbolos = var_simbolos.get()

    caracteres_desejados = ""

    if incluir_numero:
        caracteres_desejados += string.digits
    if incluir_letra_minuscula:
        caracteres_desejados += string.ascii_lowercase
    if incluir_letra_maiscula:
        caracteres_desejados += string.ascii_uppercase
    if incluir_simbolos:
        caracteres_desejados += string.punctuation

    if not caracteres_desejados:
        messagebox.showerror("Erro", "Você deve selecionar pelo menos um tipo de caractere.")
    else:
        senha = ''.join(random.choices(caracteres_desejados, k=qtd_caracteres_senha))
        entry_senha.config(show="*")
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)

def alternar_visibilidade():
    if entry_senha.cget("show") == "*":
        entry_senha.config(show="")
        botao_visibilidade.config(text="Ocultar")
    else:
        entry_senha.config(show="*")
        botao_visibilidade.config(text="Mostrar")

def copiar_senha():
    senha = entry_senha.get()
    if senha:
        janela.clipboard_clear()
        janela.clipboard_append(senha)
        janela.update() 
        messagebox.showinfo("Copiado", "Senha copiada com sucesso")
    else:
        messagebox.showwarning("Aviso", "Não há nenhuma senha para copiar.")


#Criação do tk
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("1200x800")

#Qtd de caracteres
label_qtd = tk.Label(janela, text="Quantidade de caracteres:")
label_qtd.place(x=420, y=220)

entry_qtd = tk.Entry(janela, width=10)
entry_qtd.place(x=570, y=222)

#Opções para selecionar
var_numero = tk.BooleanVar()
var_minuscula = tk.BooleanVar()
var_maiscula = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

check_numero = tk.Checkbutton(janela, text="Incluir números", variable=var_numero)
check_numero.place(x=420, y=280)

check_minuscula = tk.Checkbutton(janela, text="Incluir letras minúsculas", variable=var_minuscula)
check_minuscula.place(x=420, y=310)

check_maiscula = tk.Checkbutton(janela, text="Incluir letras maiúsculas", variable=var_maiscula)
check_maiscula.place(x=420, y=340)

check_simbolos = tk.Checkbutton(janela, text="Incluir símbolos", variable=var_simbolos)
check_simbolos.place(x=420, y=370)

#Gerar senha
botao_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha)
botao_gerar.place(x=420, y=410)

#Exibir a senha gerada
label_senha = tk.Label(janela, text="Senha Gerada:")
label_senha.place(x=420, y=480)

entry_senha = tk.Entry(janela, state="normal", width=30, show="*")
entry_senha.place(x=510, y=480)


botao_visibilidade = tk.Button(janela, text="Mostrar", command=alternar_visibilidade)
botao_visibilidade.place(x=530, y=520)

botao_copiar = tk.Button(janela, text="Copiar Senha", command=copiar_senha)
botao_copiar.place(x=600, y=520)


janela.mainloop()




#AJEITAR TUDO PRA FICAR NO MEIO