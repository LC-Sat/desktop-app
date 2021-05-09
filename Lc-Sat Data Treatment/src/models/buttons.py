# -*- coding: utf-8 -*-

try:
	print("Chargement fichier buttons.py")
	import tkinter as tk
	from tkinter import ttk

except Exception as e:

	raise e


# Class de liaison entre les différents bouttons

class Buttons:


	def __init__(self):

		self.browse_folder_button = Browse_Folder_Button()
		self.valid_button = Valid_Button()
		self.normal_button = Normal_Button()


	def __str__(self):

		return "Class Bouttons"


# Bouttons de recherche de fichier

class Browse_Folder_Button:


	def __str__(self):

		return "Class Browse Bouttons"


	def create_widget(self, parent, text):

		button = tk.Button(parent, text=text, width=25, font=('Arial', 20, 'bold'))
		return button


# boutton valider

class Valid_Button:


	def __str__(self):

		return "Class Valid Bouttons"


	def create_widget(self, parent, text):

		button = tk.Button(
			parent,
			text=text,
			background="#1e8449",
			foreground="#F0F8FF",
			font=('Arial', 20, 'bold'),
			width=25
			)
		return button


# boutton normal

class Normal_Button:


	def __str__(self):

		return "Class Normal Button"


	def create_widget(self, parent, text):
		
		button = tk.Button(parent, text=text, font=('Arial', 15), width=20)
		return button


print("Fin Chargement fichier buttons.py")