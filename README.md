[![Build Status](https://travis-ci.org/franfermi/Infraestructura-Virtual_IV.svg?branch=master)](https://travis-ci.org/franfermi/Infraestructura-Virtual_IV)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/apps/subjectsgii)

[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

![Docker: OK](https://dockerbuildbadges.quelltext.eu/status.svg?organization=niccokunzmann&repository=dockerhub-build-status-image)

[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

# SubjectsGII_Bot

## Descripción general

El proyecto que voy a realizar trata de un bot desarrollado en Python, que mostrará información sobre asignaturas del grado de Ingeniería Informática de la ETSIIT. La información se almacenará en una base de datos, en ésta se encontrará el siguiente contenido:

* Guía docente de las asignaturas.

* Horarios de los distintos grupos.

* Fecha de exámenes finales.

## Requerimientos

Debido a que el desarrollo se realizará en Python, necesitaremos las librerías, API o framework correspondientes.

Los datos sobre cada una de las asignaturas de alojarán en algún sitio.

## Servicios

* Base de datos Postgres.

* API Bot Telegram para la comunicación.

## Automatización

He realizado un fichero *Makefile* que se encargará de automatizar el proceso.

## Integración continua

El sistema de integración continua que he utilizado es *Travis-CI*, enlazado con mi cuenta de GitHub. Este sistema comprueba de forma continua cada cambio que es realizado en el repositorio para que todo funcione correctamente. Su fichero de configuración es *.travis.yml*.

## Despliegue en un PaaS

Para mi proyecto he empleado el PaaS [Heroku](https://www.heroku.com/).

Los pasos a seguir para su despliegue son los siguientes:

-Instalamos el cliente de heroku desde su propia página o mediante el siguiente comando:

<code>wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh</code>

-Una vez instalado, procedemos a autenticarnos en heroku.

<code>heroku login</code>

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/heroku_login.png)

-Creamos la aplicación la cual vamos a desplegar.

<code>heroku apps:create --region eu subjectsgii</code>

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/create_app_heroku.png)

-Añadimos los siguientes ficheros:

* [Procfile](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/Procfile), fichero de ejecución de Heroku. Worker para el servicio bot de Telegram y Web para el servicio web desplegado.
* [runtime.txt](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/runtime.txt), especificamos la versión de python utilizada.
* [requierements.txt](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/requirements.txt), añadimos las dependencias de nuestro proyecto.

-Desplegamos Github desde Heroku para un despliegue automático:

En la opción de despliegue de Heroku, en métodos de despliegue seleccionamos la opción Github.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/metodo_despliegue.png)

Conectamos nuestro repositorio Github en el cual se encuentra nuestro proyecto.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/conexi%C3%B3n_github.png)

Por último activamos el despliegue automático y activamos la opción de que antes de desplegar debe de pasar el test de Travis.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/despligue_aut_Travis.png)

-Para configurar el token de Telegram para su uso desde Heroku:

<code>heroku config:set TOKEN=$$$$ --app subjectsgii</code>

-Por último, lanzamos tanto el bot como el servicio web.

<code>heroku ps:scale worker=1 --app subjectsgii</code>

<code>heroku ps:scale web=1 --app subjectsgii</code>

-Comprobamos que están activos y funcionando.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/gunicorn_API_web.png)

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/worker_web_funcionando.png)

* Servicio Web: https://subjectsgii.herokuapp.com/

* Bot Telegram: @proyecto_iv_bot

Despliegue https://subjectsgii.herokuapp.com/

## Despliegue en Docker

Para desplegar nuestro proyecto en [Docker](https://www.docker.com/), nos creamos una cuenta y un repositorio, a este último le asociaremos nuestro proyecto de Github.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/repositorio_docker.png)

Como siguiente paso sería activar las compilaciones automáticas, para que cada vez que hagamos <code>push</code> se compile también en Docker.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/build_configurations.png)

Para el despliegue necesitaremos añadir a nuestro repositorio el archivo [Dockerfile](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/Dockerfile), (pinchando en el enlace podemos ver su contenido).

Una vez configurado correctamente incluyendo las variables de entorno para el accceso a la BD y el token para el bot de Telegram, Docker comenzará a construir un contenedor con los comandos que se encuentran en el archivo.

Para comprobar que todo ha ido correctamente, se mostrará lo siguiente:

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/despliegue_Docker.png)

Ya está todo listo para descargar nuestro contenedor con el comando:

<code>sudo docker build -t subjectsgii_bot ./</code>

(Para no hacer uso de "sudo" debemos de seguir el siguiente [tutorial](https://docs.docker.com/engine/installation/linux/linux-postinstall/#manage-docker-as-a-non-root-user) proporcionado por el profesor).

Una vez descargada la imagen de Docker podemos comprobar que realmente se encuentra con:

<code>docker images</code>

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/imagen_docker.png)

Repositorio en DockerHub: https://hub.docker.com/r/franfermi/subjectsgii_bot/

## Despliegue en Azure

El despliegue en [Azure](https://azure.microsoft.com/es-es/) lo he realizado mediante Azure Cloud Shell que es un shell de Bash que se puede ejecutar directamente en Azure Portal.

El primer paso sería crear un grupo de recursos en el cual se implementan y administran los recursos de las aplicaciones desarrolladas.

<code>az group create --name proyectoIV --location "West Europe"</code>

El segundo paso es crear un plan de App Service de Linux, en mi caso he utilizado un plan de precios estándar en un contenedor Linux.

<code>az appservice plan create --name AppServicePlan --resource-group proyectoIV --sku S1 --is-linux</code>

Como tercer paso, creamos la aplicación web en el plan de servicio creado, en este paso tenemos que añadir la imagen de nuestro contenedor, para ello indicamos su *docker-ID* seguido del nombre de la imagen.

<code>az webapp create --resource-group proyectoIV --plan AppServicePlan --name subjectsgiibot --deployment-container-image-name 422e56bd4839/subjectsgii_bot</code>

Por último, configuramos las variables de entorno que en este caso será el puerto que usará la aplicación, para no tener conflictos con el puerto 80, he utilizado el puerto 8000.

<code>az webapp config appsettings set --resource-group proyectoIV --name subjectsgiibot --settings WEBSITES_PORT=8000</code>

Servicio web desplegado:

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/azure_funcionando.jpg)

Contenedor: https://subjectsgiibot.azurewebsites.net/

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

La explicación con detalle de los pasos que he seguido para el despliegue se encuentran en:

[Documentación Hito 5](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/Documentaci%C3%B3n_final.md)

El contenido de los ficheros utilizados para el despliegue son:

[var.yml](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/var.yml)

[playbook.yml](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/provision/playbook.yml)

[ansible.cfg](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/ansible.cfg)

[Vagrantfile](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/Vagrantfile)

Para el despliegue he utilizado Fabric y he configurado varias opciones en el fichero fabfile.py para que se puedan realizar remotamente.

[fabfile.py](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/despliegue/fabfile.py)

Para realizar la instalación de nuestra máquina, usamos vagrant con nuestro Vagrantfile configurado.

<code>vagrant up --provider=azure</code>

Una vez terminado el proceso de instalación, nos vamos a Azure y comprobamos que efectivamente se ha creado la máquina virtual.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/maquina_creada.png)

Una vez creada nuestra máquina virtual, le abrimos el puerto 80 en la configuración de red de nuestra máquina.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/puerto_abierto.png)

Para finalizar, cambiamos el nombre del dominio.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/config_dns.png)

Un ejemplo de funcionamiento sería:

<code>fab -H vagrant@subjectsgii.southcentralus.cloudapp.azure.com IniciarApp
</code>

![culr](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/docs/img/servicio_funcionando.png)

Despliegue final: http://subjectsgii.southcentralus.cloudapp.azure.com/