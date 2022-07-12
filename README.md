# Web Django
Esta, es una página web básica de **mascotas**, tiene las siguientes características que permite ingresas datos de los principales modelos (mascota, cliente, veterinario) así como buscar mascotas en base a su nombre y desplegar los datos de las mascotas con nombre similar:

## Modelos:
Mascota:

| Campos | Descripción                                   |
|--------|------------------------------------|
| Nombre | Nombre de la mascota               |
| Edad   | Edad en años de la mascota         |
| Tipo   | Tipo de mascota (perro, gato, etc.)|

Cliente:

| Campos | Descripción                                   |
|--------|------------------------------------|
| Nombre | Nombre de la mascota               |
| Apelido   | Edad del cliente                |
| Email   | Email del cliente                 |

Veterinario:

| Campos | Descripción                                   |
|--------|------------------------------------|
| Nombre | Nombre del veterinario               |
| Especialidad   | Especialidad del veterinario (en perros, gatos, etc.)                |

## Templates:
| HTML | Descripción |
|------|-------------|
|inicio.html| Página de inicio |
|**padre.html**| *padre* del resto de páginas|
|cliente.html| Página de cliente
|clienteFormulario.html| Formulario de ingreso de datos del cliente |
|mascota.html| Página de mascota
|mascotaFormulario.html| Formulario de ingreso de datos de mascotas|
|veterinario.html| Página de veterinario|
|veterinarioFormulario.html| Formulario de Ingreso de datos del veterinario
| busquedaMascota.html| Busca las mascotas con un nombre similar al ingresado |
| resultadosBusqueda.html| Muestra el resultados de las búsqueda de las mascotas

## Navegación
Ingrese a: http://127.0.0.1:8000/App/
Los links a Inicio, Mascota, Cliente y Veterinario por lo pronto no realizan ninguna funcionalidad más que dirigirse a la página.html respectiva.

En el siguiente texto "xxxx" tiene que actualizarse con el nombre de la página respectiva:

> Este es el contenido de **xxxx** tiene que actualizarse

- En el link MascotaFormulario puede ingresar una mascota.

- En el link ClienteFormulario puede ingresar un cliente.

- En el link VeterinarioFormulario puede ingresar un veterinario.

- En el link BusquedaMascota puede buscar los datos de las mascotas en base al nombre que se digite.




