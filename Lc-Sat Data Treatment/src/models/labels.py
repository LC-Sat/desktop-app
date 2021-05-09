# -*- coding: utf-8 -*-

try:
	print("Chargement fichier labels.py")
	import tkinter as tk
	from tkinter import ttk

except Exception as e:
	raise e

# class de liaison

class Labels:


	def __init__(self):

		self.label_title = Label_Title()
		self.subtitle_label = Subtitle()
		self.label_classic = Label_Classic()
	

	def __str__(self):

		return "Class Labels"


	def label_title(self, text):

		return self.label_title.create_widget(text)


	def classic_label(self, text):

		return self.label_classic.create_widget(parent, text)



# Label Titre

class Label_Title:


	def create_widget(self, parent, text, background, color):

		label = ttk.Label(parent, text=text, background=background, foreground=color, font="Impact 50 bold", padding=50)
		return label


# Label Sous-Titre

class Subtitle:


	def create_widget(self, parent, text, background, color):

		label = ttk.Label(parent, text=text, background=background, foreground=color, font="Arial 15 bold",justify='left')
		return label


# Label text classique

class Label_Classic:


	def create_widget(self, parent, text, background, color):
		
		label = ttk.Label(parent, text=text, background=background, foreground=color, font="Arial 30 bold", justify='left')
		return label


print("Fin Chargement fichier labels.py")