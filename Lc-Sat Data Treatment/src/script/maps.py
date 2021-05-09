# -*- coding: utf-8 -*-

try:
	print("Démarrage du fichier map")
	import folium
	import webbrowser

except Exception as e:
	raise e


# class de liaison

class Map:


	def __init__(self):

		self.planisphere_map = Planisphere_Map()
		self.schematic_map = Schematic_Map()
		self.terrain_map = Terrain_Map()


	def __str__(self):

		return "Class Map"



class Planisphere_Map:


	def __str__(self):

		return "Marker Map class"


	def render_map(self, latitude, longitude, store_path):

		self.map = folium.Map(location=[latitude[0], longitude[0]], zoom_start=13)

		for i in range(len(latitude)):

			try:

				folium.Marker(
				    location=[latitude[i], longitude[i]],
				    icon=folium.Icon(color="red", icon="info-sign"),
				).add_to(self.map)

				print("Marker {0} :\tlat = {1}\tlon = {2}".format(i, latitude[i], longitude[i]))

			except IndexError:

				break


		# affiche la carte dans le navigateur
		self.map.save(store_path + "planisphere.html")
		self.url = store_path + "planisphere.html"
		webbrowser.open(self.url, new=2)



class Schematic_Map:


	def __str__(self):

		return "Class Schematic Map"


	def render_map(self, latitude, longitude, store_path):

		self.map = folium.Map(location=[latitude[0], longitude[0]], zoom_start=13, tiles="Stamen Toner")

		for i in range(len(latitude)):

			try:

				folium.Marker(
				    location=[latitude[i], longitude[i]],
				    icon=folium.Icon(color="red", icon="info-sign"),
				).add_to(self.map)

				print("Marker {0} :\tlat = {1}\tlon = {2}".format(i, latitude[i], longitude[i]))

			except IndexError:

				break


		# affiche la carte dans le navigateur
		self.map.save(store_path + "schematic.html")
		self.url = store_path + "schematic.html"
		webbrowser.open(self.url, new=2)



class Terrain_Map:


	def __str__(self):

		return "Class Terrain Map"


	def render_map(self, latitude, longitude, store_path):

		self.map = folium.Map(location=[latitude[0], longitude[0]], zoom_start=13, tiles="Stamen Terrain")

		for i in range(len(latitude)):

			try:

				folium.Marker(
				    location=[latitude[i], longitude[i]],
				    icon=folium.Icon(color="red", icon="info-sign"),
				).add_to(self.map)

				print("Marker {0} :\tlat = {1}\tlon = {2}".format(i, latitude[i], longitude[i]))

			except IndexError:

				break


		# affiche la carte dans le navigateur
		self.map.save(store_path + "terrain.html")
		self.url = store_path + "terrain.html"
		webbrowser.open(self.url, new=2)


print("Fin Démarrage du fichire map")


# class Map terrain vue satellite 
# class Map terrain vu schéma