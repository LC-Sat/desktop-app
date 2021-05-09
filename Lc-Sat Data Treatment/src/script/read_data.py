# -*- coding: utf-8 -*-

try:
	print("Chargement fichier read_data.py")
	import pickle
	import numpy as np
	import json
	import cv2 as cv
	from cv2 import VideoWriter, VideoWriter_fourcc


except Exception as e:
	raise e

# lit et enregistre les données des fichiers décryptés dans des arrays numpy


class Data_Reader:

	def __init__(self, folder_path):

		self.folder_path = folder_path


	def __str__(self):

		return "Data Reader"


	def read_data(self):

		# Reconvertit les données et les enregistres dans des arrays numpy en "float64"
		data = pickle.load(open(self.folder_path + "data.bin", "rb"))

		self.pression = np.array(data["press"], dtype="float64")
		self.temperature = np.array(data["temp"], dtype="float64")
		self.altitude = np.array(data["alt"], dtype="float64")
		self.x_acceleration = np.array(data["ax"], dtype="float64")
		self.y_acceleration = np.array(data["ay"], dtype="float64")
		self.z_acceleration = np.array(data["az"], dtype="float64")
		self.latitude = np.array(data["lat"], dtype="float64")
		self.longitude = np.array(data["lon"], dtype="float64")
		self.satellite = np.array(data["sat"], dtype="float64")
		self.quality = np.array(data["qual"], dtype="float64")
		self.speed = np.array(data["speed"], dtype="float64")
		# self.humidity = np.array(data["hum"])
		 
		try:
			self.thermique = np.array(data["therm"], dtype="float64")

		except KeyError:

			self.thermique = np.array(0, dtype="float64")

		# Créer une vidéo à partir du tableau de pixels
		


		print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t".format(self.pression, self.temperature, self.altitude, self.x_acceleration, self.y_acceleration, self.z_acceleration, self.latitude, self.longitude, self.satellite, self.quality, self.speed, self.thermique))


	def return_all_data(self):

		return [self.pression, self.temperature, self.altitude, self.x_acceleration,self.y_acceleration, self.z_acceleration, self.satellite, self.quality, self.speed]

# Transforme le tableau de pixel en video
class Thermal_Video:


	def __str__(self):

		return "Thermal Video Maker Class"


	def __init__(self, config_path, store_path):

		# Charge les consantes depuis le fichier de configuration
		with open(config_path, "r") as file:

			config = json.load(file)

			file.close()


		self.MIN_TEMP = [config["MIN_TEMP"], config["MIN_COLOR"]]
		self.MAX_TEMP = [config["MAX_TEMP"], config["MAX_COLOR"]]
		self.MOY_TEMP = [(self.MIN_TEMP[0] + self.MAX_TEMP[0]) / 2, config["MOY_COLOR"]]

		self.WIDTH = config["RESOLUTION"][0]
		self.HEIGHT = config["RESOLUTION"][1]

		self.FPS = config["FPS"]

		self.store_path = store_path

		self.FINAL_RESOLUTION = [config["FINAL_RESOLUTION"][0], config["FINAL_RESOLUTION"][1]]

	def convert_to_color(self, value):

		# Détermination du ratio à appliquer pour changer la couleur
		# 0 <= couleur <= 255
		# Renvoi la couleur RGB du pixel

		if value < MOY_TEMP[0]:

			ratio = (self.MOY_TEMP[0] + self.MIN_TEMP[0] + value) / 300
			return [
				round((self.MOY_TEMP[1][0] + self.MIN_TEMP[1][0]) * ratio),
				round((self.MOY_TEMP[1][1] + self.MIN_TEMP[1][1]) * ratio),
				round((self.MOY_TEMP[1][2] + self.MIN_TEMP[1][2]) * ratio)
			]

		elif value > MOY_TEMP[0]:

			ratio = (self.MOY_TEMP[0] + self.MIN_TEMP[0] + value) / 300
			return [	
				round((self.MOY_TEMP[1][0] + self.MAX_TEMP[1][0]) * ratio),
				round((self.MOY_TEMP[1][0] + self.MAX_TEMP[1][0]) * ratio),
				round((self.MOY_TEMP[1][0] + self.MAX_TEMP[1][0]) * ratio)
			]

		else:

			return self.MOY_TEMP[1]


	def resize_thermal_video(self):

		cap = cv.VideoCapture(self.store_path + 'thermal.avi')
		fourcc = cv.VideoWriter_fourcc(*'XVID')
		out = cv.VideoWriter('output.avi', fourcc, 5, (self.FINAL_RESOLUTION[0], self.FINAL_RESOLUTION[1]))

		while True:

		    ret, frame = cap.read()

		    if ret == True:

		        b = cv.resize(frame, (440, 440), fx=0, fy=0, interpolation = cv.INTER_CUBIC)
		        out.write(b)

		    else:

		        break

		cap.release()
		out.release()
		cv.destroyAllWindows()


	def create_thermal_video(self, data):

		# Transforme la valeur de temperature des pixels en une valeur RGB
		# Ecrit cette valeur dans  

		fourcc = VideoWriter_fourcc(*'MP42')	
		video = VideoWriter(self.store_path +'thermal.avi', fourcc, float(self.FPS), (self.WIDTH, self.HEIGHT))

		for frame in data["therm"]:

			colored_image = []

			for row in frame:

				colored_row = []

				for pixel in row:

					colored_image.append(self.convert_to_color(pixel))

				colored_image.append(colored_row)

			image = np.uint8(colored_image)

			video.write(image)

		video.realease()

		self.resize_thermal_video()



print("Fin Chargement fichier read_data.py")