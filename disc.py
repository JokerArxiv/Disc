import os
from tkinter import *

def sair_janela():
	janela.destroy()

def arquivo_abrir_janela():
	pass

def arquivo_salvar_janela():
	pass

def geolocalizador():

	def sair_janela_geolocalizador():
		janela_geolocalizador.destroy()	

	def buscar():
		pass

	janela_geolocalizador = Tk()		

	# Configuraçãp da Janela
	janela_geolocalizador.title("Geolocalizador | DISC ")
	janela_geolocalizador.geometry("800x500+250+100")

	# Barra de Janela
	barra_menu_geolocalizador = Menu(janela_geolocalizador)
	janela_geolocalizador.config(menu = barra_menu_geolocalizador)

	# Barra de Menu
	arquivo_geolocalizador = Menu(barra_menu_geolocalizador)
	arquivo_geolocalizador.add_command(label = "Salvar")
	arquivo_geolocalizador.add_separator()
	arquivo_geolocalizador.add_command(label = "Sair", command = sair_janela_geolocalizador)
	barra_menu_geolocalizador.add_cascade(label = "Arquivo", menu = arquivo_geolocalizador)

	Label(janela_geolocalizador, text = "Host: ").place(x = 0, y = 0)
	Host = Entry(janela_geolocalizador)
	Host.place(x = 35, y = 0)
	btn_geolocalizador_play = Button(janela_geolocalizador,text = "Buscar", command = buscar)

def pesquisa_pessoas():

	def sair_janela_pesquisa():
		janela_pesquisa.destroy()

	def buscar():
		pass	

	janela_pesquisa = Tk()

	# Configuração da Janela
	janela_pesquisa.title("Pesquisa | DISC ")
	janela_pesquisa.geometry("800x500+250+100")

	# Barra de Janela
	barra_menu_pesquisa = Menu(janela_pesquisa)
	janela_pesquisa.config(menu = barra_menu_pesquisa)

	# Barra de Menu
	arquivo_pesquisa = Menu(barra_menu_pesquisa)
	arquivo_pesquisa.add_command(label = "Salvar")
	arquivo_pesquisa.add_separator()
	arquivo_pesquisa.add_command(label = "Sair", command = sair_janela_pesquisa)
	barra_menu_pesquisa.add_cascade(label = "Arquivo", menu = arquivo_pesquisa)

	Label(janela_pesquisa, text = "Pessoa: ").place(x = 0, y = 0)
	Pessoa = Entry(janela_pesquisa)
	Pessoa.place(x = 47, y = 0)
	btn_pesquisa_play = Button(janela_pesquisa, text = "Buscar", command = buscar)

janela = Tk()

# Barra de Janela
barra_menu = Menu(janela)
janela.config(menu = barra_menu)

# Configuração da Janela
janela.title("Departamento de Inteligencia e Seguranca Cibernética")
janela.geometry("800x500+250+100")

# Barra de Menu
arquivo = Menu(barra_menu)
arquivo.add_command(label = "Abrir", command = arquivo_abrir_janela)
arquivo.add_command(label = "Salvar", command = arquivo_salvar_janela)
arquivo.add_separator()
arquivo.add_command(label = "Sair", command = sair_janela)
barra_menu.add_cascade(label = "Arquivo", menu = arquivo)

# Frase de Introdução
Introducao = Label(janela, text = "Departamento de Inteligencia e Seguranca Cibernética")
Introducao.place(x = 240, y = 0)

# Geolocalizador
btn_geolocalizador = Button(janela, text = "Geolocalizador", command = geolocalizador) 
btn_geolocalizador.place(x = 1, y = 30)

# Pesquisa de pessoas
btn_pesquisa = Button(janela, text = "Pesquisa de Pessoas", command = pesquisa_pessoas)
btn_pesquisa.place(x = 1, y = 70)

janela.mainloop()
