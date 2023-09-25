# TerceraPreEntrega-Canton
A continuación dejo las funcionalidades de la página web creada:
El objetivo de la misma es tener un registro en la database de Libros, Peliculas y Canciones.
He creado un buscador de Libros por género. Y cada una de las navbar, tienen un boton para ingresar al html de los formularios.


Ejecuta las migraciones de Django con el comando: python manage.py migrate. Ejecuta el servidor con el comando: python manage.py runserver. 
Abre un navegador y navega hasta http://127.0.0.1:8000/AppCoder/ para ver la página principal. En ella se de ta la bienvenida y se te indica el buscador de libros, por género.
En el margen superior se encuentran las 3 navbar correspondientes a los modelos creados. (Libros, Musica y Peliculas)
Si accede a alguno de ellos se le redigirá a la url de cada uno pudiendo ser: http://127.0.0.1:8000/AppCoder/libro/ , http://127.0.0.1:8000/AppCoder/musica/ , http://127.0.0.1:8000/AppCoder/peliculas/ .
Dentro de estas url se encuentra un botón que dirige al url de los formularios de cada models. Se encontrará con un input, donde se le solicitarán datos que se guardarán en la base de datos del proyecto.
Para poder visualizar los datos almacenados que no sean de Libros(Ya que para éste tiene un buscador en el http://127.0.0.1:8000/AppCoder). Puede ingresar al url http://127.0.0.1:8000/admin con el superuser creado: - User: Martin Password: Tincho1889 -

Saludos atte.
Martín Cantón

