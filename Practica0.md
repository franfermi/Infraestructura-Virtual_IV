# **Práctica 0**: *Git y GitHub para entrega de hitos del proyecto*.

## Creación de par de claves y subida de clave pública a GitHub.

Para la creación de par de claves, escribimos desde nuestro terminal el siguiente comando:

`ssh-keygen -t rsa -C "franfermi@correo.ugr.es"`

Se nos pedirá el lugar donde queremos almacenar el archivo que contendrá
nuestra clave, por defecto se almacena en /home/<nombre_usuario>/.ssh/id_rsa.

Para subir nuestra clave pública a GitHub, mostramos el contenido de dicha clave que se encuentra en la ruta anterior para posteriormente copiarlo a nuestra cuenta GitHub.

`cat id_rsa.pub`

En nuestro perfil de GitHub vamos a Settings/SSH and GPG keys/New SSH key. En el campo "key" copiamos nuestra clave pública.

Para comprobar que funciona correctamente realizamos una conexión mediante ssh, si todo va bien mostrará un mensaje de bienvenida. 

`ssh -T git@github.com`

## Configuración correcta del nombre y correo electrónico para que aparezca en los commits.

## Edición del perfil en GitHub para que aparezca nombre completo y ciudad, así como universidad.

