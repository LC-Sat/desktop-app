# -*- coding: utf-8 -*-

try:
	print("Chargement fichier crypt.py")
	import pyAesCrypt
	import shutil
	import zipfile
	import os

except Exception as e:
	raise e


# décompresse le fichier + décrypt les fichiers du dossier

class Decrypt:


	def __str__(self):

		return "Decrypt class"


	# Décrypt le fichier
	def decrypt(self, folder_path, destination, data_type, password):

		print("\n")

		print("\tCHEMIN : " + folder_path)
		print("\tDESTINATION : " + destination)

		# print("chemin fichier :{0}\nchemin destination: {1}\ntype_donnée: {2}\nmdp: {3}".format(folder_path, destination, data_type, password))

		filename, file_extension = os.path.splitext(folder_path)

		print("\tFILENAME : " + filename)
		print("\tFILE EXTENSION : " + file_extension)

		print("\n")

		destination = destination + '/data/'

		# Décompresse le fichier
		if file_extension == '.gz' or file_extension == '.zip':
			
			shutil.unpack_archive(folder_path, destination)

		# Transfert les fichiers si le dossier est déjà décompressé
		else:

			for filename in os.listdir(folder_path):

				print("\t FILENAME : " + filename)
				shutil.copyfile(filename, destination)
			print("\n")

		 # Décrypte chaque fichier:
		 # 	- key est le nom initial
		 # 	- value est le nom final

		for key, value in data_type.items():

			print("\tKEY : " + key)
			print("\tVALUE : " + value)
			print("\tPASSWORD : " + password)

			print("\n")

			if os.path.exists(key):
				pyAesCrypt.decryptFile(key, value, password, 16 * 1024)


print("Fin Chargement fichier crypt.py")