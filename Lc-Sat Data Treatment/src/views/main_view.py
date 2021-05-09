# -*- coding: utf-8 -*-

try:
	print("Chargement fichier main_view.py")
	import tkinter as tk
	from tkinter import ttk

except Exception as e:
	raise e

# Page d'import et de décryptage des données
 
class Main_Window:


	def __init__(self, controllers, models, scripts):
		
		self.controllers = controllers
		self.models = models
		self.scripts = scripts


	def __str__(self):

		return "Load Data Window class"


	# Détruits les anciens widgets lorsque un nouvel onglet est appelé
	def clear_widgets(self):

		try:
			self.content_frame.destroy()

		except Exception:
			pass


	# ================
	# 	  Cartes
	# ================

	def render_planishpere_map(self):

		self.scripts.maps.planisphere_map.render_map(
			self.latitude,
			self.longitude,
			self.controllers.path_controller.get_path("FILES_DATA")
			)


	def render_shematic_map(self):

		self.scripts.maps.schematic_map.render_map(
			self.latitude,
			self.longitude,
			self.controllers.path_controller.get_path("FILES_DATA")
			)

	
	def render_terrain_map(self):

		self.scripts.maps.terrain_map.render_map(
			self.latitude,
			self.longitude,
			self.controllers.path_controller.get_path("FILES_DATA")
			)


	def show_map_tab(self):

		self.clear_widgets()

		self.latitude = self.scripts.read_data.latitude
		self.longitude = self.scripts.read_data.longitude

		# affiche les différents bouttons
		self.content_frame = tk.Frame(
			bg=self.controllers.theme_controller.get_theme("backgroundColor"),
			borderwidth=5,
			highlightbackground=self.controllers.theme_controller.get_theme("color"),
			highlightcolor=self.controllers.theme_controller.get_theme("color"),
			highlightthickness=5
			)
		self.content_frame.grid(row=0, column=1, padx=25, pady=25)

		self.map_title = self.models.labels.subtitle_label.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("map"),
			self.controllers.theme_controller.get_theme("backgroundColor"),
			self.controllers.theme_controller.get_theme("color")
			)
		self.map_title.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

		self.planisphere_button = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("planisphere")
			)
		self.planisphere_button.configure(command=self.render_planishpere_map)
		self.planisphere_button.grid(row=1, column=0, padx=10, pady=10)

		self.schematic_button = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("schematic")
			)
		self.schematic_button.configure(command=self.render_shematic_map)
		self.schematic_button.grid(row=1, column=1, padx=10, pady=10)
		
		self.terrain_button = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("satellite")
			)
		self.terrain_button.configure(command=self.render_terrain_map)
		self.terrain_button.grid(row=1, column=2, padx=10, pady=10)


	# ================
	# Camera classique
	# ================


	# Affiche la vidéo standart 
	def render_clasic_video(self):

		self.scripts.videos.classic_video.render(self.controllers.path_controller.get_path("FILES_DATA") + "cam.mp4")


	# Affiche la video avec filtrage des mouvements
	def motion_filtering_video(self):

		self.scripts.videos.motion_filtering.render(self.controllers.path_controller.get_path("FILES_DATA") + "cam.mp4")


	# Affiche le contour des objets en mouvement de la caméra classique
	def classic_video_motion_detection(self):

		self.scripts.videos.motion_detection.render(self.controllers.path_controller.get_path("FILES_DATA") + "cam.mp4")


	# ================
	# Camera thermique
	# ================

	def render_thermal_video(self):

		self.scripts.videos.classic_video.render(self.controllers.path_controller.get_path("FILES_DATA") + "output.avi")


	# Affiche l'ensemble des fonctionnalités 
	def show_video_tab(self):

		self.clear_widgets()

		# Création des labels des catégories
		self.content_frame = tk.Frame(
			bg=self.controllers.theme_controller.get_theme("backgroundColor"),
			borderwidth=5,
			highlightbackground=self.controllers.theme_controller.get_theme("color"),
			highlightcolor=self.controllers.theme_controller.get_theme("color"),
			highlightthickness=5
			)
		self.content_frame.grid(row=0, column=1, padx=25, pady=25)

		self.classic_camera_label = self.models.labels.subtitle_label.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("classicVideo"),
			self.controllers.theme_controller.get_theme("backgroundColor"),
			self.controllers.theme_controller.get_theme("color")
			)
		self.classic_camera_label.grid(row=0, column=0, padx=10, pady=10)

		self.thermal_camera_label = self.models.labels.subtitle_label.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("thermialVideo"),
			self.controllers.theme_controller.get_theme("backgroundColor"),
			self.controllers.theme_controller.get_theme("color")
			)
		self.thermal_camera_label.grid(row=0, column=1, padx=10, pady=10)

		# ================
		# Camera classique
		# ================

		# Affiche la vidéo classique sans outils d'analyse
		self.classic_video_tracking_button = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("showNormalVideo")
			)
		self.classic_video_tracking_button.configure(command=self.render_clasic_video)
		self.classic_video_tracking_button.grid(row=1, column=0, padx=10, pady=10)

		# Affiche la vidéo classique avec detourage des mouvements
		self.classic_video_render_button = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("renderTrackingVideo")
			)
		self.classic_video_render_button.configure(command=self.classic_video_motion_detection)
		self.classic_video_render_button.grid(row=2, column=0, padx=10, pady=10)

		# Affiche la vidéo classique avec filtrage des mouvements 
		self.classic_video_motion_button = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("renderMotionFiltering")
			)
		self.classic_video_motion_button.configure(command=self.motion_filtering_video)
		self.classic_video_motion_button.grid(row=3, column=0, padx=10, pady=10)

		# ================
		# Camera thermique
		# ================

		# Affiche la vidéo thermique sans outils d'analyse
		self.classic_video_tracking_button = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("showNormalVideo")
			)
		self.classic_video_tracking_button.configure(command=self.render_thermal_video)
		self.classic_video_tracking_button.grid(row=1, column=1, padx=10, pady=10)

		# ==== Fonctionnalites non developee ! ====

		# Affiche la vidéo thermique avec detourage des mouvements
		# self.classic_video_render_button = self.models.buttons.normal_button.create_widget(self.content_frame, self.controllers.language_controller.get_text("renderTrackingVideo"))
		# self.classic_video_render_button.configure(command=self.test)
		# self.classic_video_render_button.grid(row=2, column=1)

		# # Affiche la vidéo thermique avec filtrage des mouvements
		# self.classic_video_motion_button = self.models.buttons.normal_button.create_widget(self.content_frame, self.controllers.language_controller.get_text("renderMotionFiltering"))
		# self.classic_video_motion_button.configure(command=self.test)
		# self.classic_video_motion_button.grid(row=3, column=1)


	# ================
	# 	 Graphiques
	# ================
	
	# ~~ Graphiques Simples


	# Affiche le graphique de l'evolution de la temperature en fonction du temps
	def render_temperature_graph(self):

		self.scripts.graphs.normal_graph.create_grah(
				self.scripts.read_data.temperature,
				"temperature",
				self.controllers.language_controller
			)


	# Affiche le graphique de l'evolution de la pression en fonction du temps
	def render_pression_graph(self):

		self.scripts.graphs.normal_graph.create_grah(
				self.scripts.read_data.pression,
				"pression",
				self.controllers.language_controller
			)


	# Affiche le graphique de l'evolution de l'altitude en fonction du temps
	def render_altitude_graph(self):

		self.scripts.graphs.normal_graph.create_grah(
				self.scripts.read_data.altitude,
				"altitude",
				self.controllers.language_controller
			)


	# Affiche le graphique de l'evolution du nombre de satellite détectés en fonction du temps
	def render_satellite_graph(self):

		self.scripts.graphs.normal_graph.create_grah(
				self.scripts.read_data.satellite,
				"satellite",
				self.controllers.language_controller
			)


	# Affiche le graphique de l'evolution de la qualité du signal en fonction du temps
	def render_quality_graph(self):

		self.scripts.graphs.normal_graph.create_grah(
				self.scripts.read_data.quality,
				"quality",
				self.controllers.language_controller
			)

	# Affiche le graphique de l'evolution de la vitesse en fonction du temps
	def render_speed_graph(self):

		self.scripts.graphs.normal_graph.create_grah(
				self.scripts.read_data.speed,
				"speed",
				self.controllers.language_controller
			)


	# ~~ Graphiques Multiples
	
	def render_acceleration_graph(self):

		self.scripts.graphs.multiple_graph.create_graph(
				[self.scripts.read_data.x_acceleration, self.scripts.read_data.y_acceleration, self.scripts.read_data.z_acceleration],
				["X", "Y", "Z"],
				"accelerometre"
			)


	# ~~ Graphiques Complets
	 
	def render_full_graph(self):

		self.scripts.graphs.full_graph.create_graph(
			self.scripts.read_data.return_all_data(),
			["Pression", "Temperature", "Altitude", "Acceleration X", "Acceleration Y", "Acceleration Z", "Satellite", "Signal quality", "Speed"]
			)


	def show_graph_tab(self):

		self.clear_widgets()

		self.content_frame = tk.Frame(
			bg=self.controllers.theme_controller.get_theme("backgroundColor"),
			borderwidth=5,
			highlightbackground=self.controllers.theme_controller.get_theme("color"),
			highlightcolor=self.controllers.theme_controller.get_theme("color"),
			highlightthickness=5
			)
		self.content_frame.grid(row=0, column=1, padx=25, pady=25)

		# labels
		self.normal_graphs_label = self.models.labels.subtitle_label.create_widget(
			self.content_frame,	
			self.controllers.language_controller.get_text("normalGraph"),
			self.controllers.theme_controller.get_theme("backgroundColor"),
			self.controllers.theme_controller.get_theme("color")
			)
		self.normal_graphs_label.grid(row=0, column=0, padx=10, pady=10)

		self.multiple_graphs_label = self.models.labels.subtitle_label.create_widget(
			self.content_frame,	
			self.controllers.language_controller.get_text("multipleGraph"),
			self.controllers.theme_controller.get_theme("backgroundColor"),
			self.controllers.theme_controller.get_theme("color")
			)
		self.multiple_graphs_label.grid(row=0, column=1, padx=10, pady=10)

		self.full_graphs_label = self.models.labels.subtitle_label.create_widget(
			self.content_frame,	
			self.controllers.language_controller.get_text("fullGraph"),
			self.controllers.theme_controller.get_theme("backgroundColor"),
			self.controllers.theme_controller.get_theme("color")
			)
		self.full_graphs_label.grid(row=0, column=2, padx=10, pady=10)

		# bouttons normal graph
		
		self.temperature_graph = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("temperature")
			)
		self.temperature_graph.configure(command=self.render_temperature_graph)
		self.temperature_graph.grid(row=1, column=0, padx=10, pady=10)

		self.pression_graph = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("pression")
			)
		self.pression_graph.configure(command=self.render_pression_graph)
		self.pression_graph.grid(row=2, column=0, padx=10, pady=10)

		self.altitude_graph = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("altitude")
			)
		self.altitude_graph.configure(command=self.render_altitude_graph)
		self.altitude_graph.grid(row=3, column=0, padx=10, pady=10)

		self.satellite_graph = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("satellite")
			)
		self.satellite_graph.configure(command=self.render_satellite_graph)
		self.satellite_graph.grid(row=4, column=0, padx=10, pady=10)

		self.quality_graph = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("quality")
			)
		self.quality_graph.configure(command=self.render_quality_graph)
		self.quality_graph.grid(row=5, column=0, padx=10, pady=10)

		self.speed_graph = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("speed")
			)
		self.speed_graph.configure(command=self.render_speed_graph)
		self.speed_graph.grid(row=6, column=0, padx=10, pady=10)

		# bouttons mutliple graph
		
		self.acceleration_graph = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("acceleration")
			)
		self.acceleration_graph.configure(command=self.render_acceleration_graph)
		self.acceleration_graph.grid(row=1, column=1, padx=10, pady=10)

		# bouttons full graph

		self.full_graph = self.models.buttons.normal_button.create_widget(
			self.content_frame,
			self.controllers.language_controller.get_text("fullGraph")
			)
		self.full_graph.configure(command=self.render_full_graph)
		self.full_graph.grid(row=1, column=2, padx=10, pady=10)


	def create_side_menu(self):

		self.side_menu = self.models.menus.side_menu.create_widget(
			self.controllers.BASE_DIR + self.controllers.path_controller.get_path("IMG_PATH"),
			self.controllers.language_controller,
			self.controllers.theme_controller.get_theme("backgroundColor"),
			self.controllers.theme_controller.get_theme("color")
			)
		
		self.models.menus.side_menu.video_btn.configure(command=self.show_video_tab)
		self.models.menus.side_menu.graph_btn.configure(command=self.show_graph_tab)
		self.models.menus.side_menu.gps_btn.configure(command=self.show_map_tab)

		self.side_menu.grid(row=0, column=0, padx=30, pady=30)


	def create_widget(self):
		
		self.scripts.read_data.read_data()

		#self.window_title = self.models.labels.label_title(self.controllers.language_controller.get_text("treatmentTools"))
		#self.window_title.grid(row=1, column=0)

		self.create_side_menu()



print("Fin Chargement fichier main_view.py")