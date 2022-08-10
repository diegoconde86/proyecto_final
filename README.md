
# Web Django
este es un blog destinado a que los usuarios puedan ingresar los datos de sus mascotas, compartir sus experiencias

-la pagina esta diseñada para que solo los usuarios registrados puedan acceder a los articulos que en ella se encuntran, los mismos una vez ingresados pueden crear su propio articulo y compartir las caracteristicas de sus mascotas y todo lo que han vivio con ellas

-Solo los usuarios registrados como administradores tienen acceso a modificar y eliminar las publicaciones de todos los usuarios ya registrados

-cada usuario que se registre tendra un avatar predeterminado el cual se puede modificar al lado de su nombre en la barra de navegacion en el boton "Editar Perfil"

-dentro de los diferentes botones que se encuentran en la barra de navegacion tenemos todo lo que podemos ver dentro de nuestra pagina incluyendo una seccion dedicada a los creadores del blog

-Esta misma pagina cuenta con un chat integrado el cual funciona para poder enviar mensajes a los diferentes usuarios que se hayan creado, enviandose al instante, dichos mensajes se guardan dentro de la base de datos

-Nosotros los creadores del blog trabajamos en conjunto en reuniones programando al tiempo y asesorandonos de manera conjunta, es una pagina que se ha formado de las bases de los conocimientos de todos los integrantes

## Modelos:
Mascota:

| Campos | Descripción                        |
|--------|------------------------------------|
| Nombre | Nombre de la mascota               |
| Edad   | Edad en años de la mascota         |
| Tipo   | Tipo de mascota (perro, gato, etc.)|
| Autor  | Autor del posteo (usuario)         |
| Fecha  | Fecha de creacion                  |
| Imagen | Imagen que acompaña al texto       |

Articulo:

| Campos    | Descripción                         |
|-----------|-------------------------------------|
| titulo    | Tiulo del posteo                    |
| subtitulo | Subtitulo del posteo                |
| cuerpo    | Texto del posteo de blog            |
| autor     | Autor del posteo (usuario)          |
| fecha     | Fecha de creacion                   |
| editado   | Usuario que modifico                |
| imagen    | Imagen que acompaña al texto        |

Avatar:

| Campos | Descripción                                   |
|--------|------------------------------------|
| User   | Nombre de usuario                  |
| Imagen | Imagen asociada al usuario         |

