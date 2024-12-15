# GESTOR DE TAREAS PYTHON

Este es un mini proyecto de un gestor de tareas desarrollado en python

---

## Configuración

Este proyecto utiliza los siguiente:

- SQLAlchemy
- Tkinter

### Instalación del Proyecto

Crear y activar un entrono virtual:

```bash
python -m venv env

env\Scripts\activate
```

Para instalar las dependencias se debe ejecutar en la terminal:

```bash
pip install -r requirements.txt
```

### Instrucciones para la Base de Datos

Se debe crear una base de datos llamada task_manager. En este proyecto se utilizó PostgreSQL

```bash
CREATE DATABASE task_manager;
```

### Instrucciones para Variables de Entorno

Se debe crear un archivo .env con el string de conexión a la base de datos.

```bash
DB_URL=DDBB://USER:PASSWORD@HOST/NAME
```

### Instrucciones para Ejecutar el Proyecto

Para ejecutar el proyecto por consola:

```bash
python main.py
```

---

## Uso de la aplicación

### Vista general de la aplicación

![Vista general](img/image.png)

- ### Para crear una nueva tarea

![Nueva tarea](img/image-1.png)

- ### Ver las tareas

![Lista de tareas](img/image-2.png)

- ### Modificar una tarea

Haciendo click en **Marcar como realizada**, la tarea cambiará de estado a _Completada_. Haciendo click en **Eliminar**, la tarea se eliminará.

- ### Ver una tarea

Al hacer doble click en una tarea se abre una nueva ventana con la información de la tarea.

![Detalle de tarea](img/image-3.png)

[Ver Informe de SonarQube](docs/task_manager%20-%20Overview%20-%20SonarQube%20Community%20Build.pdf)
