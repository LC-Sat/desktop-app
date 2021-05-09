# -*- coding: utf-8 -*-s

try:
	print("Chargement fichier video.py")
	import cv2 as cv
	import matplotlib.pyplot as plt
	import numpy as np

except Exception as e:
	raise e


# class liaison avec l'interface

class Video:

	def __init__(self):

		self.classic_video = Render_Video()	
		self.motion_filtering = Video_Motion_Filtering()
		self.motion_detection = Motion_Detection()


# Affiche la vidéo sans changements
class Render_Video:

	def render(self, video_path):

		cap = cv.VideoCapture(video_path)

		# Read until video is completed
		while(cap.isOpened()):
		    
		    # Capture frame-by-frame
		    ret, frame = cap.read()
		    
		    if ret == True:

		        # Display the resulting frame
		        cv.imshow('Frame', frame)

		    # Press Q on keyboard to  exit
		    if cv.waitKey(25) & 0xFF == ord('q'):
		        break

		# When everything done, release the video capture object
		cap.release()

		# Closes all the frames
		cv.destroyAllWindows()


# Filtrage des formes en mouvements sur la vidéo
class Video_Motion_Filtering:

	def render(self, video_path):

		# variables
		substractor_min = 20
		substractor_max = 50

		# charge la video et les composants nécéssaires pour le filtrage des mouvements 
		video = cv.VideoCapture(video_path)
		substractor = cv.createBackgroundSubtractorMOG2(20, 50)

		# Recherche si la vidéo est toujours en cours:
		# 	- si oui, applique le détourage tant que la touche 'x' n'est pas pressée
		# 	- si non, relance la vidéo

		while True:

			return_value, frame = video.read()

			if return_value:

				mask = substractor.apply(frame)
				cv.imshow('Mask', mask)

				# changement des variables
				key = cv.waitKey(30)&0xFF
				
				if key == ord('x'):
					break

				if key == ord('p'):

					substractor_max = min(100, substractor_max + 5)

				if key == ord("m"):

					substractor_min = max(5, substractor_min - 5)

			else:
				
				video = cv.VideoCapture(video_path)



		video.release()
		cv.destroyAllWindows()


# Detourage des formes en mouvements
class Motion_Detection:

	def render(self, video_path):

		# Chargement de la video
		capture = cv.VideoCapture(video_path)

		# Valeurs d'analyse
		kernel_blur = 1
		seuil = 15
		surface = 1000

		# Video sans changement des variables d'analyse
		ret, origin = capture.read()

		origin = cv.cvtColor(origin, cv.COLOR_BGR2GRAY)
		origin = cv.GaussianBlur(origin, (kernel_blur, kernel_blur), 0)

		kernel_dilate = np.ones((5, 5), np.uint8)

		while True:

			# Video avec changement des variables d'analyse
			ret, frame = capture.read()

			gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
			gray = cv.GaussianBlur(gray, (kernel_blur, kernel_blur), 0)
			cv.imshow("frame", gray)

			# Comparaison des deux flux videos
			mask = cv.absdiff(origin, gray)
			mask = cv.threshold(mask, seuil, 255, cv.THRESH_BINARY)[1]
			mask = cv.dilate(mask, kernel_dilate, iterations=3)

			# Ajout des contours des objets en mouvement
			contours, nada = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
			frame_contour = frame.copy()

			for c in contours:

				cv.drawContours(frame_contour, [c], 0, (0, 255, 0), 5)

				if cv.contourArea(c)< surface:

					continue

				x, y, w, h = cv.boundingRect(c)
				cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

			origin = gray

			# Ajout des textes
			cv.putText(frame, "[o|1]seuil: {:d} [p|m]blur: {:d} [i|k]surface: {:d}".format(seuil, kernel_blur, surface), (10, 30), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
			# Affichage du resultat
			
			cv.imshow("frame", frame)

			# Changement des variables
			key = cv.waitKey(30)&0xFF

			if key == ord('x'):

				break
			
			try:

				if key == ord('p'):

					kernel_blur = min(43, kernel_blur + 2)

				if key == ord('m'):

					kernel_blur = max(1, kernel_blur - 2)
				
				if key == ord('s'):

					surface += 100

				if key == ord('r'):

					surface -= 100

				if key == ord('o'):

					seuil = min(255, seuil + 1)

				if key == ord('l'):

					seuil = max(1, seuil - 1)

			except Exception:

				pass

		capture.release()
		cv.destroyAllWindows()

# Reconnaissance d'objets

class Video_Object_Recognition:

	def __init__(self):
		pass


print("Fin Chargement fichier video.py")