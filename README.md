# Sistema de recomendaciones
## inteligencia artifical - 2020-1

Un proyecto realizado por

  - Guzmán Mosco Mario Alexis
  - Torres Bucio Miriam
  - Martinez Mendoza Miguel Angel

# Especificaciones funcionales

Este proyecto fue realizado con las siguientes tecnologias:

| Nombre | Version | Descripción |
| ------ | ------ | ------ |
| Conda  | 4.7.10 | Ambiente virtual, manejador de paquetes para python|
| Python3 | 3.5.2 | Lenguaje de programación |
| Pip3 | 19.2.3 | Sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python |
| Django | 2.2.4 | Framework para desarrollo web |
| Numpy | 1.11.0 | Biblioteca de python para realizar operaciones aritmeticas y estadisticas |

Proyecto realizado y ejecutado en una computadora con las siguientes especificaciones: 
```sh
  Sistema operativo: Ubuntu 16.04.1 LTS
  Kernel: Linux 4.4.0-142-generic
  Architectura: x86-64
```

# Uso

Para usar este proyecto es necesario un ambiente virtual de python en este caso se usa conda para crear el ambiente. Para crear el ambiente con la version de python que se necesita es con el siguiente comando:

```sh
$ conda create -n myenv python=3.5
```
en donde myenv es el nombre del ambiente. El ambiente instalara junto con python una version acorde de pip y de sqllite que también se necesitará para la ejecución, se obtentra el siguiente mensaje al cual hay que aceptar:

```sh
The following NEW packages will be INSTALLED:

  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main
  ca-certificates    pkgs/main/linux-64::ca-certificates-2019.10.16-0
  certifi            pkgs/main/linux-64::certifi-2018.8.24-py35_1
  libedit            pkgs/main/linux-64::libedit-3.1.20181209-hc058e9b_0
  libffi             pkgs/main/linux-64::libffi-3.2.1-hd88cf55_4
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-9.1.0-hdf63c60_0
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-9.1.0-hdf63c60_0
  ncurses            pkgs/main/linux-64::ncurses-6.1-he6710b0_1
  openssl            pkgs/main/linux-64::openssl-1.0.2t-h7b6447c_1
  pip                pkgs/main/linux-64::pip-10.0.1-py35_0
  python             pkgs/main/linux-64::python-3.5.6-hc3d631a_0
  readline           pkgs/main/linux-64::readline-7.0-h7b6447c_5
  setuptools         pkgs/main/linux-64::setuptools-40.2.0-py35_0
  sqlite             pkgs/main/linux-64::sqlite-3.30.1-h7b6447c_0
  tk                 pkgs/main/linux-64::tk-8.6.8-hbc83047_0
  wheel              pkgs/main/linux-64::wheel-0.31.1-py35_0
  xz                 pkgs/main/linux-64::xz-5.2.4-h14c3975_4
  zlib               pkgs/main/linux-64::zlib-1.2.11-h7b6447c_3
```

una vez instalado hay que activar el ambiente nuevo

```sh
$ conda activate myenv
```
Para desactivar el ambiente el comando es:
```sh   
$ conda deactivate
```

Para más informacion ver la [documentación de Conda][df1]

Una vez activado el ambiente hay que instalar Django dentro de él con el siguiente comando: 

```sh   
$ pip install django
```
Esto instalará django es su version más reciente. Por ultimo hay que instalar la biblioteca numpy la cual es utilizada en el archvio Kmeans.py (en donde está implementado el algoritmo del mismo nombre) para calcular la distancia entre dos vectores en un espacio euclideano.

De igual forma para instalar numpy basta con hacer uso de pip

```sh   
$ pip install numpy
```

con esto es suficiente para correr el proyecto. Ahora hay que ubicarse en el directorio donde se tiene guardado el proyecto y correrlo con

```sh   
$ python3 manage.py runserver
```

Esto corre el servidor y despliega el siguiente mensaje:

```sh  
Performing system checks...

System check identified no issues (0 silenced).
November 04, 2019 - 02:24:52
Django version 2.2.6, using settings 'Proyecto3.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Por defecto se corre en el localhost en el pueto 8000, por lo que hay que abrir un navergador y correrlo desde la dirección http://localhost:8000/ 




[df1]: <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>