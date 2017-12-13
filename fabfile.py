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
	with shell_env(HOST_BD=os.environ['HOST_BD'], USER_BD=os.environ['USER_BD'], PW_BD=os.environ['PW_BD'], NAME_BD=os.environ['NAME_BD']):
		# Iniciamos el servicio web
		run('cd Infraestructura-Virtual_IV/ && python3 API_web.py')
