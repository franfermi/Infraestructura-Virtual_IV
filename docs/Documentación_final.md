# SubjectsGII_Bot

## Diseño del soporte virtual para el despliegue de una aplicación

El despliegue de la aplicación en IaaS, lo he realizado mediante la herramienta de despliegue automático [Vagrant](https://www.vagrantup.com/).

Esta herramienta se encargará de desplegar una máquina virtual que he creado en [Azure](https://azure.microsoft.com/es-es/?&WT.srch=1&wt.mc_id=AID623300_SEM_QwnrSFdW&gclid=Cj0KCQiAyNjRBRCpARIsAPDBnn0DULNnhzu_rpdyCiA0384sQUnFqJTI7rArRWFSfik1ZiTu56oi-uoaAsQeEALw_wcB) con el código promocional proporcionado por el profesor.

He seguido los siguientes pasos para el despliegue:

* Instalar Vagrant.
* Instalar Ansible.
* Configurar fichero *var.yml*.
* Configurar fichero *playbook.yml*.
* Configurar fichero *ansible.cfg*.
* Creación  y configuración de aplicación en Azure.
* Configurar fichero *Vagrantfile*.
* Instalación de la máquina virtual.
* Establecer puertos y dominios.
* Configurar fichero *fabfile.py*.

### Instalar Vagrant

Para la instalación de Vagrant, descargamos el paquete de instalación de su propia [página](https://www.vagrantup.com/downloads.html) y lo instalamos:

<code>sudo dpkg -i vagrant_<version>.deb</code>

Y por último, instalamos el plugin de Azure para Vagrant:

<code>vagrant plugin install vagrant-azure</code>

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/plugin_azure.png)

### Instalar Ansible

Para la instalación de [Ansible](https://www.ansible.com/) simplemente usamos el siguiente comando:

<code>sudo apt-get install ansible</code>

### Configurar fichero var.yml

En este fichero he declarado unas variable que necesitaré para el despliegue junto con dependencias del sistema.

~~~
---

# Variables para el despliegue
project_name: Infraestructura-Virtual_IV
project_repo: https://github.com/franfermi/Infraestructura-Virtual_IV.git
proyect_path: SubjectsGII_Bot

# Dependencias del sistema
system_packages:
  - build-essential
  - npm
  - nodejs-legacy
  - git
~~~



### Configurar fichero playbook.yml

Este fichero se encargará del provisionamiento de Ansible, instalará las dependencias del sistema, clonará nuestro repositorio e instalará los módulos necesarios para nuestra aplicación.

Todos estos datos los obtendrá del fichero *var.yml* que hemos configurado anteriormente.

~~~
---
- hosts: all
  remote_user: vagrant
  vars_files:
    - var.yml
  gather_facts: no
  become: yes
  become_method: sudo
  tasks:
    - name: Instalar paquetes del sistema
      apt: pkg={{ item }} update-cache=yes cache_valid_time=3600
      with_items: "{{ system_packages }}"

    - name: Descargar fuentes
      git: repo={{project_repo}} dest={{proyect_path}} clone=yes force=yes
    - name: Run npm install
      npm: path={{proyect_path}}
~~~

### Configurar fichero ansible.cfg

He añadido este fichero para evitar posibles errores durante el proceso de provisionamiento que se pueden producir con cadenas demasiado largas..

~~~
[ssh_connection]
control_path = %(directory)s/%%h-%%p-%%r
~~~

### Creación  y configuración de aplicación en Azure

Una vez tengamos una cuenta activa en Azure, procedemos a instalar el cliente en nuestro equipo para así poder crear los certificados de seguridad para sincronizarnos con nuestra máquina.

<code>sudo npm install -g azure-cli</code>

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/azure_cli.png)

Ahora ya podemos hacer login desde nuestra terminal.

<code>azure login</code>

Al hacer login se nos proporciona un código, dicho código debemos de introducirlo en la web de Azure para verificar la autentificación.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/azure_login.png)

Entramos en modo *asm*, es el modo de gestión de servicios de Azure.
Esto lo realizamos para poder descargamos el archivo publishSettings.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/mode_asm.png)

Descargamos el archivo con <code>azure account download</code>.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/account_down.png)

Y por último, importamos el archivo descargado a nuestra cuenta Azure.

<code>azure account import ./Pase para Azure-11-28-2017-credentials.publishSettings</code>

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/publicSettings.png)

Una vez tengamos los fichero necesarios, obtenemos los certificados de seguridad.

<code>openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout azurevagrant.key -out azurevagrant.key</code>

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/cert1.png)

~~~
chmod 600 azurevagrant.key
openssl x509 -inform pem -in azurevagrant.key -outform der -out azurevagrant.cer
~~~

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/cert2.png)

Tras estos pasos, hemos obtenido un fichero .cer que será nuestro certificado. Acto siguiente será subirlo a nuestra cuenta de Azure, en certificados de administración.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/cert_azure.png)

Llegados a este punto ya podemos registrar nuestra nueva aplicación en Azure Active Directory.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/registro_app.png)

Ya tenemos nuestra aplicación creada, ahora si hacemos click en ella podemos obtener la información que necesitaremos para configurar el fichero Vagrantfile, los datos que necesitamos son los siguientes:

* AZURE_CLIENT_ID: Id. de aplicación.

* AZURE_CLIENT_SECRET: En acceso de API/Claves generamos una clave para nuestra aplicación y copiamos su contenido.

* AZURE_TENANT_ID: En las propiedades de Azure Active Directory, obtenemos el Id. de directorio.

* AZURE_SUBSCRIPTION_ID: En Suscripciones, obtenemos el id de la suscripción.

Como último paso, creamos en Control de Acceso (IAM) un nuevo usuario con el rol de colaborador, este usuario estará asociado a nuestra aplicación anteriormente creada y contendrá los permisos para la creación de la máquina virtual.

### Configurar fichero Vagrantfile

El contenido de mi fichero Vagrantfile es el siguiente:

~~~
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|

  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box' #Caja base vacía
  config.vm.network "private_network",ip: "192.168.11.4", virtualbox__intnet: "vboxnet0" #Ip privada
  config.vm.hostname = "localhost"
  config.vm.network "forwarded_port", guest: 80, host: 80

  # use local ssh key to connect to remote vagrant box
  config.vm.provider :azure do |azure, override|
    config.ssh.private_key_path = '~/.ssh/id_rsa'
    azure.vm_image_urn = 'canonical:UbuntuServer:16.04-LTS:16.04.201701130' #Imagen base del sistema
    azure.vm_size = 'Basic_A0' #Tamaño (recursos) de la MV
    azure.location = 'southcentralus'
    azure.tcp_endpoints = '80:80'
    azure.vm_name = "maquinaSubjectsGII"
    azure.resource_group_name= "subjectsgiibot"
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']
  end

  # Provisionar con ansible
  config.vm.provision "ansible" do |ansible|
    ansible.sudo = true
    ansible.playbook = "./provision/playbook.yml"
    ansible.verbose = "-vvvv"

    ansible.host_key_checking = false
  end

end
~~~

### Instalación de la máquina virtual

Para realizar la instalación de nuestra máquina, usamos vagrant con nuestro Vagrantfile configurado.

<code>vagrant up --provider=azure</code>

Una vez terminado el proceso de instalación, nos vamos a Azure y comprobamos que efectivamente se ha creado la máquina virtual.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/maquina_creada.png)

### Establecer puertos y dominios

Una vez creada nuestra máquina virtual, le abrimos el puerto 80 en la configuración de red de nuestra máquina.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/puerto_abierto.png)

Para finalizar, cambiamos el nombre del dominio.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/config_dns.png)


### Configurar fichero fabfile.py

Para el despliegue he utilizado Fabric y he configurado varias opciones en el fichero fabfile.py para que se puedan realizar remotamente.

El contenido de mi fichero es el siguiente:

~~~
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
		run('cd ~/Infraestructura-Virtual_IV/ && sudo -E python3 API_web.py',pty=False)
~~~

Un ejemplo de funcionamiento sería:

<code>fab -H vagrant@subjectsgii.southcentralus.cloudapp.azure.com IniciarApp
</code>

![culr](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/servicio_funcionando.png)
