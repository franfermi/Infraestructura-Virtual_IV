# coding: utf-8

from fabric.api import sudo, cd, env, run, shell_env
import os


def InstalarApp():
	""" Función para descargar el bot del repositorio. """
	# Descargamos el repositorio
	run('git clone https://github.com/franfermi/Infraestructura-Virtual_IV.git')

	# Instalamos pip3	
	run('sudo apt-get install -y python3-pip')

	# Accedemos al repositorio e instalamos las dependencias
	run('cd Infraestructura-Virtual_IV/ && pip3 install -r requirements.txt')

def BorrarApp():
	""" Función para borrar el repositorio. """
	# Borramos el repositorio
	run('sudo rm -rf ./Infraestructura-Virtual_IV')

def IniciarApp():
	""" Función para iniciar la web. """
	# Importamos las variables globales
	with shell_env(HOST_BD="ec2-54-247-81-97.eu-west-1.compute.amazonaws.com", USER_BD="kteqeodcirfqvw", PW_BD="3ebd9387410d8aa87910d06e9976392ea4108ca9c91df01603e3ee7ceadf1c66", NAME_BD="d7qsuf34inh34t"):
		# Iniciamos el servicio web
		run('cd ~/Infraestructura-Virtual_IV/ && sudo -E python3 API_web.py',pty=False)
