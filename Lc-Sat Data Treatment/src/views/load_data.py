# -*- coding: utf-8 -*-

try:
	print("Chargement fichier load_data.py")
	import tkinter as tk
	from tkinter import filedialog

except Exception as e:
	raise e


# Page d'import et de décryptage des données
 
class Load_Data_Window:


	def __init__(self, controllers, models):
		
		self.controllers = controllers
		self.models = models
	

	def __str__(self):

		return "Load Data Window class"


	# Gère l'affichage du chemin du dossier sélectionné
	def folder_path(self):

		self.filename = filedialog.askopenfilename(defaultextension='.gz', initialdir ="Téléchargements")
		self.path_label.configure(text=self.filename)


	# créer les composants
	def create_widget(self, parent):
		
		# titre
		self.title = self.models.labels.label_title.create_widget(parent,
			self.controllers.language_controller.get_text("loadData"),
			self.controllers.theme_controller.get_theme("backgroundColor"),
			self.controllers.theme_controller.get_theme("color")
			)
		self.title.pack()

		# Frame du formulaire
		 
		self.form_frame = tk.Frame(parent,
			bg=self.controllers.theme_controller.get_theme("backgroundColor"),
			borderwidth=5,
			highlightbackground=self.controllers.theme_controller.get_theme("color"),
			highlightcolor=self.controllers.theme_controller.get_theme("color"),
			highlightthickness=5,
			)
		self.form_frame.pack()

		# indicateur d'enter de clef de décryptage
		self.key_input_indicator = self.models.labels.label_classic.create_widget(self.form_frame,
		 	self.controllers.language_controller.get_text("keyInput"),
			self.controllers.theme_controller.get_theme("backgroundColor"),
			self.controllers.theme_controller.get_theme("color")
			)
		self.key_input_indicator.configure(padding=35)
		self.key_input_indicator.pack()

		# Champs de saisie de la clef de décryptage
		self.key_input = self.models.inputs.entry.create_widget(self.form_frame)
		self.key_input.pack()

		# indicateur d'enter de clef de décryptage
		self.folder_path_indicator = self.models.labels.label_classic.create_widget(self.form_frame,
			self.controllers.language_controller.get_text("folderInput"),
			self.controllers.theme_controller.get_theme("backgroundColor"),
			self.controllers.theme_controller.get_theme("color")
			)
		self.folder_path_indicator.configure(padding=35)
		self.folder_path_indicator.pack()

		# boutton de selection de fichier
		self.browse_folder = self.models.buttons.browse_folder_button.create_widget(
			self.form_frame,
			self.controllers.language_controller.get_text("browse")
			)
		self.browse_folder.configure(command=self.folder_path)
		self.browse_folder.pack()

		# Chemin du fichier choisi
		self.path_label = self.models.labels.subtitle_label.create_widget(self.form_frame,
			'',
			self.controllers.theme_controller.get_theme("backgroundColor"),
			self.controllers.theme_controller.get_theme("color")
			)
		self.path_label.pack()


print("Fin Chargement fichier load_data.py")