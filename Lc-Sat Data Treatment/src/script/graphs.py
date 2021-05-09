# -*- coding: utf-8 -*-

try:

	import matplotlib.pyplot as plt
	from matplotlib.widgets import CheckButtons
	import numpy as np
	import json

except Exception as e:

	raise e


# Class de liaison

class Graph:


	def __str__(self):

		return "Graph class"


	def __init__(self, data_config_path):

		self.data_config_path = data_config_path
		self.normal_graph = Normal_Graph(self.data_config_path)
		self.multiple_graph = Multiple_Graph(self.data_config_path)
		self.full_graph = Full_Graph(self.data_config_path)


# Trace l'evolution d'une seule mesure

class Normal_Graph:


	def __init__(self, data_config_path):

		with open(data_config_path, "r") as file:
			
			self.data_config = json.load(file)
			file.close()


	def __str__(self):

		return "Normal class Graph"


	def create_grah(self, data, data_name, language_controller):

		# valeur x et y du graph
		x = [0]
		y = []
		
		# frequence de l'enregistrement
		x_step = 1 / self.data_config[data_name]["fps"]

		for _ in range(len(data) - 1):

			x.append(x_step)
			x_step += x_step

		X = np.array(x)
		Y = np.array(data, dtype="float64")

		# configuration des graphiques
		
		plt.plot(X, Y, 'r-+')
		plt.xlabel(language_controller.get_text("time"))
		plt.ylabel(self.data_config[data_name]["name"] + ' (' + self.data_config[data_name]["unit"] + ")")

		plt.title(self.data_config[data_name]["name"] + ' ' + language_controller.get_text("overTime"))
		plt.show()



# Trace l'evolution d'un ensemble de mesures de meme type

class Multiple_Graph:


	def __init__(self, data_config_path):

		with open(data_config_path, "r") as file:
			
			self.data_config = json.load(file)
			file.close()


	def __str__(self):

		return "Multiple Graph Class"


	def create_graph(self, data, data_names, data_type):

		# Creation des 'sous' graphiques
		fig, axs = plt.subplots(len(data))
		fig.suptitle(self.data_config[data_type]["name"] + " en fonction du temps.")

		for i, unit in enumerate(data):

			x = []
			x_step = 1 / self.data_config[data_type]["fps"]


			for _ in range(len(unit)):

				x.append(x_step)
				x_step += x_step

			X = np.array(x)
			Y = np.array(unit, dtype="float64")

			axs[i].plot(X, Y, '-o', label=data_names[i])
			axs[i].legend(data_names[i])

		plt.show()


# Trace toutes les mesures

class Full_Graph:


	def __init__(self, data_config_path):

		with open(data_config_path, "r") as file:
			
			self.data_config = json.load(file)
			file.close()


	def __str__(self):

		return "Full Graph Class"


	def create_graph(self, datas, data_names):


		fig, ax = plt.subplots()

		# FPS
		x_step  = 1 / 10

		lines = []

		for i, data in enumerate(datas):

			x = []

			for _ in range(len(data)):

				x.append(x_step)
				x_step += x_step

			X = np.array(x)
			Y = np.array(data, dtype="float64")

			print(len(X))
			print(len(Y))
			i, = ax.plot(X, Y, label=data_names[i])
			lines.append(i)

		rax = plt.axes([0.05, 0.4, 0.1, 0.15])
		labels = [str(line.get_label()) for line in lines]
		visibility = [line.get_visible() for line in lines]
		check = CheckButtons(rax, labels, visibility)


		def change_visivility(label):

		    index = labels.index(label)
		    lines[index].set_visible(not lines[index].get_visible())
		    plt.draw()


		check.on_clicked(change_visivility)

		plt.show()