# **Práctica 0**: *Git y GitHub para entrega de hitos del proyecto*.

## Creación de par de claves y subida de clave pública a GitHub.

Para la creación de par de claves, escribimos desde nuestro terminal el siguiente comando:

`ssh-keygen -t rsa -C "franfermi@correo.ugr.es"`

Se nos pedirá el lugar donde queremos almacenar el archivo que contendrá nuestra clave, por defecto se almacena en /home/<nombre_usuario>/.ssh/id_rsa.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/hito0/Capturas/clave_generada.png)

Para subir nuestra clave pública a GitHub, mostramos el contenido de dicha clave que se encuentra en la ruta anterior para posteriormente copiarlo a nuestra cuenta GitHub.

`cat id_rsa.pub`

En nuestro perfil de GitHub vamos a Settings/SSH and GPG keys/New SSH key. En el campo "key" copiamos nuestra clave pública.
Para comprobar que funciona correctamente realizamos una conexión mediante ssh, si todo va bien mostrará un mensaje de bienvenida.

`ssh -T git@github.com`

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/hito0/Capturas/conexi%C3%B3n_ssh.png)

## Configuración correcta del nombre y correo electrónico para que aparezca en los commits.

Para configurar el nombre y correo electrónico de nuestra cuenta de GitHub para que aparezca en los commit usaríamos:

`git config --global user.name "Francisco Fernández Millán"`
`git config --global user.email "franfermi@correo.ugr.es"`

## Edición del perfil en GitHub para que aparezca nombre completo y ciudad, así como universidad.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/hito0/Capturas/perfil_github.png)

Tras completar nuestro perfil procedemos a la creación del repositorio de la asignatura pulsando "Add repository" en la pagina principal.
En mi caso se llama Infraestructura-Virtual_IV, de forma pública y lo inicializamos con README.

## Clonación del repositorio de la asignatura

Para enlazar nuestra cuenta GitHub con el repositorio de la asignatura usamos la opción **Fork** de dicho repositorio. Con esto ya lo tenemos enlazado, lo siguiente es pasar los archivos a nuestro equipo en local con el comando:

`git clone git@github.com:franfermi/IV-17-18.git`

## Creación de una rama en nuestro repositorio

En nuestro repositorio trabajaremos con diferentes ramas, en cada una de las cuales desarrollaremos los distintos hitos, en este caso crearemos el hito0.

`git checkout -b hito0`

Una vez creada, cambiamos a dicha rama y comprobamos que nos encontramos en hito0.

`git branch`

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/hito0/Capturas/cambio_rama.png)

Ya podemos subir nuestros archivos de la siguiente forma:

`git add Practica0.md`
`git commit -m "Subida Practica0, actualizacion 1"`
`git push origin hito0`

## Creación y cierre de milestones e issues

En primer lugar creamos nuestro primer Milestones, en mi caso será la entrega de la práctica 0 de la asignatura junto con la fecha de subida.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/hito0/Capturas/crear_milestone.png)

Posteriormente creamos issues asociados a nuestro milestones, que serán como tareas a realizar para completar el desarrollo de la entrega.
Conforme completemos cada issues, lo cerramos para incrementar el porcentaje a realizar para la finalización de la práctica.

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/hito0/Capturas/cierre_issue.png)

Una vez cerrado el issue, en la web se mostrará lo siguiente:

![curl](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/hito0/Capturas/cierre_issue_web.png)
